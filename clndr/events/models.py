from django.db import models

from users.models import User

EVENTS_DB = {}

class Event(models.Model):
    name = models.CharField(verbose_name='Event name', max_length=255)
    from_date = models.DateTimeField(verbose_name='Event start')
    to_date = models.DateTimeField(verbose_name='Event end')
    comment = models.CharField(verbose_name='Comment', null=True, max_length=255)
    creator = models.ForeignKey(User, verbose_name='Event creator', on_delete=models.CASCADE)
