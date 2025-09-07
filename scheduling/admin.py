from django.contrib import admin
from .models import Shift
# Register your models here.

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['event','assigned_employee']