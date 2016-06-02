from django.shortcuts import render
from .models import Meetings, Nutritionist
import json
from django.core import serializers
from django.http import JsonResponse
from .forms import MeetingForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage

from django.views.generic import TemplateView, View
from django.shortcuts import get_list_or_404
# Create your views here.

class Home(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        # dispatch takes care of "reading" the parameters from the url
        self.nutritionists = get_list_or_404(Nutritionist) # I would use some kind of default value to prevent exception, but its up to your logic
        return TemplateView.dispatch(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # get_context_data creates the context
        title = 'dietetycy'
        context = TemplateView.get_context_data(self, **kwargs)
        context.update({"title": title, "nutritionists": self.nutritionists})

        return context

class Calendar(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        # dispatch takes care of "reading" the parameters from the url
        meetings = get_list_or_404(Meetings)  # I would use some kind of default value to prevent exception, but its up to your logic
        url = request.get_full_path()
        n_id = url[-1:]
        self.dataToCal = {
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': []
        }
        # filling fields in calendar
        for day in range(1, 6):
            day = str(day)
            for meeting in meetings:
                if meeting.day == day and str(meeting.nutritionist.id) == n_id:
                    hourBegin = meeting.hourBegin
                    hourEnd = meeting.hourEnd
                    self.dataToCal[day].append([hourBegin, hourEnd])

        self.dataToCal = json.dumps(self.dataToCal)
        return TemplateView.dispatch(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # get_context_data creates the context
        title = 'kalendarz'
        context = TemplateView.get_context_data(self, **kwargs)
        context.update({'title': title, 'dataToCal': self.dataToCal})

        return context

class Send_form(TemplateView):

    def post(self, request, *args, **kwargs):
        url = request.get_full_path()
        day = url[-7:-6]
        n_id = url[-1:]
        hourBegin = url[-6:-1].encode('ascii','ignore')
        hourEnd = hourBegin
        hourEnd = list(hourEnd)

        # creating hour of end from hour of begin
        if hourEnd[3] == '0':
            hourEnd[3] = '3'
        elif hourEnd[3] == '3':
            if hourEnd[1] == '9' and hourEnd[0] == "0":
                hourEnd[0] = "1"
                hourEnd[1] = "0"
                hourEnd[3] = '0'
            elif hourEnd[1] == '9' and hourEnd[0] == "1":
                hourEnd[0] = "2"
                hourEnd[1] = "0"
                hourEnd[3] = '0'
            else:
                hourEnd[1] = str(int(hourEnd[1]) + 1)
                hourEnd[3] = '0'
        hourEnd = "".join(hourEnd)
        nutritionist = Nutritionist.objects.get(pk=n_id)


        meeting_hourBegin = hourBegin
        meetting_hourEnd = hourEnd
        meeting_day = day
        meeting_name = request.POST.get('the_name')
        meeting_fullname = request.POST.get('the_fullname')
        meeting_email = request.POST.get('the_email')
        meeting_nutritionist = nutritionist

        meeting = Meetings(
            hourBegin=meeting_hourBegin,
            hourEnd=meetting_hourEnd ,
            day=meeting_day ,
            name=meeting_name ,
            fullname=meeting_fullname ,
            email=meeting_email ,
            nutritionist=meeting_nutritionist
        )
        meeting.save()

        response_data = {}
        response_data['hourBegin'] = meeting.hourBegin
        response_data['hourEnd'] = meeting.hourEnd
        response_data['day'] = meeting.day
        response_data['name'] = meeting.name
        response_data['fullname'] = meeting.fullname
        response_data['email'] = meeting.email
        response_data['nutritionist'] = meeting.nutritionist.id

        days = {
            '1': 'poniedzialek',
            '2': 'wtorek',
            '3': 'sroda',
            '4': 'czwartek',
            '5': 'piatek'
        }
        email = EmailMessage("Potwierzenie rejestracji",
                             'Witaj {}! Zarejestrowales sie do {} {} {} w najblizszy {} o godznie {}'.
                             format(meeting_name.encode('ascii','ignore'),
                                    meeting_nutritionist.title.encode('ascii','ignore'),
                                    meeting_nutritionist.name.encode('ascii','ignore'),
                                    meeting_nutritionist.fullname.encode('ascii','ignore'),
                                    days[meeting_day].encode('ascii','ignore'),
                                    meeting_hourBegin).encode('ascii','ignore'),
                             to=[meeting_email])
        email.send()
        print('Siemanko')
        return JsonResponse(response_data)

    def get_context_data(self, **kwargs):
        # get_context_data creates the context
        title = 'Formularz'
        form = MeetingForm()
        context = TemplateView.get_context_data(self, **kwargs)
        context.update({'title': title, 'form': form})

        return context

class Thanks(TemplateView):
    def get_context_data(self, **kwargs):
        # get_context_data creates the context
        title = 'dziekujemy'
        context = TemplateView.get_context_data(self, **kwargs)
        context.update({"title": title})

        return context
