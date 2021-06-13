from django.conf.urls import include
from django.urls import path
from . import views

app_name = 'employees_api'

urlpatterns = [
    path('employees/', views.Employees.as_view()),
    # path('assistant/<int:pk>/', assistant_views.UpdateAssistant.as_view()),
    # path('ask-question/', assistant_views.AskQuestion.as_view()),
    # path('train-assistant/', assistant_views.TrainAssistant.as_view()),
    # path('channel/', channel_views.Channel.as_view()),
    # path('channel/<int:pk>/', channel_views.UpdateChannel.as_view()),
    # path('collective/', collective_views.Collective.as_view()),
    # path('collective/<int:pk>/', collective_views.UpdateCollective.as_view()),
]