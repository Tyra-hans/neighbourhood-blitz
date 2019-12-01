from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    is_regular = models.BooleanField(default=True)

class RegularProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='regular_profile')
    bio = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
  
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='admin_profile')
    bio = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)    
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_regular:
		RegularProfile.objects.get_or_create(user = instance)
	else:
		AdminProfile.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_regular:
		instance.regular_profile.save()
	else:
		AdminProfile.objects.get_or_create(user = instance)
	