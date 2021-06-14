from django.conf.urls import include
from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'employees_api'

urlpatterns = [
    url(r'employees/(?P<date>\d{4}-\d{2}-\d{2})/$', views.AvailableEmployees.as_view()),
    url(r'meeting_slots/(?P<date>\d{4}-\d{2}-\d{2})/'
    	r'(?P<emp1_id>\d+)/'
    	r'(?P<emp2_id>\d+)/$', views.AvailableMeetingSlots.as_view()),
]