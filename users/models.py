from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
# Modified User Model
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    # This method is for creating regular users
    def create_user(self, sec_id, email, password=None, **extra_fields):
        if not sec_id:
            raise ValueError('The Security ID must be set')
        email = self.normalize_email(email)
        user = self.model(sec_id=sec_id, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
        
    def create_superuser(self, sec_id, email, password=None, **extra_fields):
        # Set default superuser flags
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True) # Superusers are typically active

        # Add validation to ensure these flags are set
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Call the create_user method (from this same CustomUserManager)
        # to handle the actual user creation logic, passing the superuser flags.
        return self.create_user(sec_id, email, password, **extra_fields)

class CustomUser(AbstractUser):
    # Creating Security Id as primary key 
    sec_id = models.PositiveIntegerField( unique=True, primary_key=True, verbose_name=("Security ID"),default=None)
    email = models.EmailField(unique=True,verbose_name=("Email address"))
    # Disable Username as primary
    username = None
    
    # Making Sec ID as Primary Key
    USERNAME_FIELD = 'sec_id'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email + ' - ' + str(self.sec_id)
    
    class Meta:
        verbose_name = ('user')
        
    @property
    def is_manager(self):
        try:
            # Check if the employee_profile (related_name) exists
            # and if its role is 'MR' (Manager Role)
            return self.employee_profile.role == "MR"  
        except Employee.DoesNotExist:
            return False 

# Data Role
STAFF_ROLES = [
    ('NR','NORMAL'),
    ('MR','MANAGER'),
    ('SR','SCHEDULER'),
    ('AD','ADMIN')
]

DEPARTMENT = [
    ('EN','EVENT'),
    ('CN','CONSIERGE')
]

class Employee(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='employee_profile')
    date_join = models.DateField(auto_now=True)
    role = models.CharField(max_length=2,choices=STAFF_ROLES,default='NR')
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=100,default='Not added')
    phone = models.PositiveBigIntegerField(default=0000000000)
    department =models.CharField(max_length=2,choices=DEPARTMENT,default='CN')
    
    def __str__(self):
        return self.user.email
    
    class Meta:
        permissions = [('can_manage','Can manage the Staff')] 