from django.db.models.signals import post_save
from .models import CustomUser,Employee
from django.dispatch import receiver

@receiver(post_save,sender=CustomUser)
def create_employee(sender,instance,created,**kwargs):
    print("create_employee signals enterd")
    
    if created  :
        Employee.objects.get_or_create(user=instance)
        print("Employee instance of", f"{instance} ", "Created")