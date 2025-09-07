from django.urls import path
from . import views 
urlpatterns = [
    path('events/',views.TicketMasterEventView.as_view()),
    # path('events_list/',views.TicketMasterEventView.as_view()),
]