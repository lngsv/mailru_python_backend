from django.urls import path

from events.views import event_details, event_list, create_event

urlpatterns = [
        path('event/', event_details, name='event_details'),
        path('list/', event_list, name='event_list'),
        path('new/', create_event, name='create_event'),
]
