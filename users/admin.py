from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Employee
from django.apps import AppConfig

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ['email']

admin.site.register(CustomUser)
admin.site.register(Employee)

