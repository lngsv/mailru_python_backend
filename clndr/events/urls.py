from django.urls import path

from events.views import event_details, event_list, create_event, update_event, delete_event

urlpatterns = [
        path('event/<int:event_id>/', event_details, name='event_details'),
        path('list/', event_list, name='event_list'),
        path('new/', create_event, name='create_event'),
        path('update/<int:event_id>/', update_event, name='update_event'),
        path('remove/<int:event_id>/', delete_event, name='delete_event'),
]
