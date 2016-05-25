from django.shortcuts import render
from .models import Meetings, Nutritionist
from django.core import serializers
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .forms import MeetingForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.mail import EmailMessage
from django.shortcuts import redirect

# Create your views here.
def home(request):
    title = 'dietetycy'
    nutritionists = Nutritionist.objects.all()
    data_json = serializers.serialize("json", nutritionists)
    return render(request, "nutritionist.html", {'title': title, 'nutritionists': nutritionists, "data_json": data_json})

def calendar(request, id=None):
    nutritionist = Nutritionist.objects.get(id=id)
    title = 'kalendarz'
    meetings = Meetings.objects.all()
    dataToCal = {
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': []
    }
    data_json = serializers.serialize("json", meetings)
    for day in range(1,6):
        day = str(day)
        for meeting in meetings:
            if meeting.day == day:
                hourBegin = meeting.hourBegin
                hourEnd = meeting.hourEnd
                # hourBegin.encode('ascii', 'ignore')
                # hourEnd.encode('ascii','ignore')
                dataToCal[day].append([hourBegin, hourEnd])
    dataToCal = json.dumps(dataToCal)
    print dataToCal
    # dataToCal = serializers.serialize("json", dataToCal)

    return render(request, "calendar.html", {'title': title, 'dataToCal': dataToCal})

@csrf_exempt
def send_form(request):
    title = 'Formularz'
    url = request.get_full_path()
    print 'xxxxxxxxxxxxxx',url
    if url[-6:-1] != "_form":
        id = url[-1:]
        hourBegin = url[-6:-1].encode('ascii','ignore')
        hourEnd = hourBegin
        hourEnd = list(hourEnd)
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
        hourEnd = "".join(hourEnd)
        print 'xxxxx', hourBegin, type(hourEnd)
    if request.method == "POST":
        meeting_hourBegin = hourBegin
        meetting_hourEnd = hourEnd
        meeting_day = request.POST.get('the_day')
        meeting_name = request.POST.get('the_name')
        meeting_fullname = request.POST.get('the_fullname')
        meeting_email = request.POST.get('the_email')
        meeting_nutritionist = request.POST.get('the_nutritionist')

        response_data = {}
        nutritionist = Nutritionist.objects.all().first()

        meeting = Meetings(
            hourBegin=meeting_hourBegin,
            hourEnd=meetting_hourEnd ,
            day=meeting_day ,
            name=meeting_name ,
            fullname=meeting_fullname ,
            email=meeting_email ,
            nutritionist=nutritionist
        )
        meeting.save()
        response_data['hourBegin'] = meeting.hourBegin
        response_data['hourEnd'] = meeting.hourEnd
        response_data['day'] = meeting.day
        response_data['name'] = meeting.name
        response_data['fullname'] = meeting.fullname
        response_data['email'] = meeting.email
        response_data['nutritionist'] = meeting.nutritionist.id
        email = EmailMessage('title', 'body', to=["john_qr@o2.pl"])
        email.send()

        return JsonResponse(response_data)
    elif request.method == "GET":
        form = MeetingForm()
        return render(request, "form.html", {'title': title, 'form': form})

def thanks(request):
    # email = EmailMessage('title', 'body', to=["john_qr@o2.pl"])
    # email.send()
    title = 'dziekujemy'
    return render(request, "thanks.html", {'title': title})

