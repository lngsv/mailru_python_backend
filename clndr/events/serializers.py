import datetime

from rest_framework import serializers

from events.models import Event
from users.models import User
from users.serializers import UserSerializer

DATETIME_FORMAT = '%Y-%m-%d %H:%M'

class EventSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(read_only=True)
    creator_id = serializers.SlugRelatedField(
        write_only=True,
        queryset=User.objects.all(),
        required=True,
        slug_field='id',
    )

    def validate(self, data):
        if not data.get('from_date') or not data.get('to_date'):
            return data

        if data['from_date'] > data['to_date']:
            raise serializers.ValidationError('from_date must be not later than to_date')
        return data

    class Meta:
        model = Event
        fields = ['id', 'name', 'from_date', 'to_date', 'creator', 'creator_id']
