from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager



class User(AbstractBaseUser, PermissionsMixin):
    
    class Meta:
        app_label = 'studentInfo'
        
    student_id = models.IntegerField()
    national_code = models.IntegerField(primary_key=True)
    cigarette_status = models.BooleanField(null=True)
    bed_time = models.CharField(max_length=15,null=True)
    tidyness_status = models.CharField(max_length=15,null=True)
    personal_type = models.CharField(max_length=10,null=True)
    email = models.EmailField(default='user@test.com')
    shared_room_id = models.IntegerField(default=0)
    
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = ['student_id', 'email']
    
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.national_code