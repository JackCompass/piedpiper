from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib.auth.models import User
from piperuser.models import UserImage
from django.db.models.signals import post_save

@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):    
	user.profile.is_online = True
	user.profile.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):   
	user.profile.is_online = False
	user.profile.save()

@receiver(post_save, sender = User)
def profileImage(sender, instance, created, **kwargs):
	if created:
		obj = UserImage.objects.create(user = instance)
		obj.save()