from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'from_date', 'to_date')

admin.site.register(Event, EventAdmin)
