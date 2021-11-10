from django.db import models
from django.urls import reverse

from users.models import User


class Event(models.Model):
    name = models.CharField(verbose_name='Event name', max_length=255)
    from_date = models.DateTimeField(verbose_name='Event start')
    to_date = models.DateTimeField(verbose_name='Event end')
    comment = models.CharField(verbose_name='Comment', null=True, blank=True, max_length=255)
    creator = models.ForeignKey(User, verbose_name='Event creator', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('event_details', kwargs=dict(event_id=self.id))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-from_date', '-to_date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
