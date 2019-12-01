from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(User):
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

class Business(models.Model):
    owner = models.ForeignKey(User, related_name="owners")
    name =models.CharField(max_length=144)
    email = models.EmailField(max_length=144)

class Police(models.Model):
    name = models.CharField(max_length=144)
    contacts = models.EmailField(max_length=144)

class Health(models.Model):
    name = models.CharField(max_length=144)
    contacts = models.EmailField(max_length=144)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=144)
    location = models.CharField(max_length=144)
    occupants_count = models.PositiveIntegerField(default=0)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    police_contacts =models.ForeignKey(Police, on_delete=models.CASCADE)
    health_contacts =models.ForeignKey(Health, on_delete=models.CASCADE)

   # neighbourhood = models.ForeignKey(Neighbourhood, related_name="neighbourhoods")
