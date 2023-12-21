from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


# when User create
@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
# when User save
@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
	profile = Profile.objects.filter(user=instance)
	if not profile:
	    Profile.objects.create(user=instance)