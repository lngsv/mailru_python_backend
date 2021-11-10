from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    def get_absolute_url(self):
        return reverse('user_details', kwargs=dict(user_id=self.id))

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
