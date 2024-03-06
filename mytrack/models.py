from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,blank=True ,null=True)
    address=models.CharField(max_length=255,blank=True, null=True)
    is_emergency_responder=models.BooleanField(default=False)
    first_name=models.CharField(max_length=30,blank=True, null=True)
    last_name=models.CharField(max_length=30,blank=True, null=True)
    
    def __str__(self):
        return self.username
from django.db import models
from mytrack.models import CustomUser

class EmergencyAlert(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.user.username}-{self.timestamp}"



    

