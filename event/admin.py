from django.contrib import admin
from .models import Event
# Register your models here.
# admin.site.register(Event)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name','venue_name','start_datetime','end_datetime')