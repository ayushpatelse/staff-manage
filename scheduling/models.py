from django.db import models
from event.models import Event
from users.models import Employee

class Shift(models.Model):
    SHIFT_STATUS = [
        ('filled','FILLED'),
        ('open','OPEN'),
        ('cancelled','CANCELLED'),
        ('completed','COMPLETED'),
    ]
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    event = models.ForeignKey(Event,blank=False,on_delete=models.DO_NOTHING,default=1)
    # location = models.ForeignKey(Location,blank=False,on_delete=models.DO_NOTHING)
    assigned_employee = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    notes = models.TextField(help_text="Optional Information",blank=True)
    status = models.CharField(choices=SHIFT_STATUS,default='open') 

