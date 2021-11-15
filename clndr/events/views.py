from datetime import datetime

from rest_framework import viewsets
from rest_framework.response import Response

from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

