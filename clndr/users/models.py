# from django.db import models
from dataclasses import dataclass

USERS_DB = {}


@dataclass
class User:
    user_id: int
    name: str
    login: str
    # pwd: str
    # events: list(Event)
