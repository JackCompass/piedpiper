from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, related_name = 'profile', on_delete = models.CASCADE)
	is_online = models.BooleanField(default = False)

# models.py
class UserImage(models.Model):
	user = models.OneToOneField(User, related_name = 'userimage', on_delete = models.CASCADE)
	avatar = models.ImageField(upload_to='images/', blank = True, null = True, default = 'avatar.png')


# from django.contrib.auth.models import User
# from piperuser.models import Profile
# obj = User.objects.get(username = 'admin')
# pobj = Profile.objects.create(user = obj)
# pobj.save()
