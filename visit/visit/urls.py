"""visit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from main.views import Home, Calendar, Send_form, Thanks
from django.conf.urls import url
from django.contrib import admin



urlpatterns = [
    url(r'^$', Home.as_view(template_name="nutritionist.html"), name='home'),
    url(r'^calendar/(?P<id>\d+)$', Calendar.as_view(template_name="calendar.html"), name='calendar'),
    url(r'^send_form/', Send_form.as_view(template_name="form.html"), name='send_form'),
    url(r'^thanks/', Thanks.as_view(template_name="thanks.html"), name='thanks'),
    url(r'^admin/', admin.site.urls),
]
