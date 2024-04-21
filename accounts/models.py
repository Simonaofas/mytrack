
from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.utils.translation import gettext as _
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
    
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     is_emergency_responder = models.BooleanField(default=False)
# #     first_name = models.CharField(max_length=30, blank=True, null=False,default='')
#     last_name = models.CharField(max_length=30, blank=True, null=False,default='')

#     # Adicione related_name aos campos groups e user_permissions
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_(
#             'The groups this user belongs to. A user will get all permissions '
#             'granted to each of their groups.'
#         ),
#         related_name='%(app_label)s_%(class)s_groups', # Define related_name
#         related_query_name="user",
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name='%(app_label)s_%(class)s_user_permissions', # Define related_name
#         related_query_name="user",
#     )

#     def __str__(self):
#         return self.username


class UserProfile(models.Model):
	'''
	Our UserProfile model extends the built-in Django User Model
	'''
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)
	town = models.CharField(verbose_name="Town/City",max_length=100, null=True, blank=True)
	county = models.CharField(verbose_name="County",max_length=100, null=True, blank=True)
	post_code = models.CharField(verbose_name="Post Code",max_length=8, null=True, blank=True)
	country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)
	longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
	latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)

	#captcha_score = models.FloatField(default = 0.0)
	has_profile = models.BooleanField(default = False)
	
	is_active = models.BooleanField(default = True)

	def __str__(self):
		return f'{self.user}'

# class EmergencyAlert(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="emergency_alerts")
#     timestamp = models.DateTimeField(auto_now_add=True)
#     message = models.TextField()
    

#     def __str__(self):
#         return f"{self.user.username}-{self.timestamp}"