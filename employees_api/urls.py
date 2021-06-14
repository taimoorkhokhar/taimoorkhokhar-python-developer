from django.conf.urls import include
from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'employees_api'

urlpatterns = [
    url(r'employees/(?P<date>\d{4}-\d{2}-\d{2})/$', views.AvailableEmployees.as_view()),
    # path('assistant/<int:pk>/', assistant_views.UpdateAssistant.as_view()),
    # path('ask-question/', assistant_views.AskQuestion.as_view()),
    # path('train-assistant/', assistant_views.TrainAssistant.as_view()),
    # path('channel/', channel_views.Channel.as_view()),
    # path('channel/<int:pk>/', channel_views.UpdateChannel.as_view()),
    # path('collective/', collective_views.Collective.as_view()),
    # path('collective/<int:pk>/', collective_views.UpdateCollective.as_view()),
]