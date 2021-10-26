# from django.db import models
from dataclasses import dataclass

EVENTS_DB = {}


@dataclass
class Event:
    event_id: int
    name: str
    from_date: str
    to_date: str
    comment: str
