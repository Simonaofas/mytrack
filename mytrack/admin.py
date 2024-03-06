from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from .models import EmergencyAlert
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(EmergencyAlert)
    

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationForm

admin.site.register(CustomUser,CustomUserAdmin)
    
    
