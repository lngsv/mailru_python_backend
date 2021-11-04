from django.db import models


USERS_DB = {}

class User(models.Model):
    name = models.CharField(verbose_name='User name', max_length=255)
    login = models.CharField(verbose_name='User login', max_length=255)
    # pwd: str
    # events: list(Event)
