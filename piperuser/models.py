from django.db import models
from django.contrib.auth.models import User

# models.py

class Profile(models.Model):
	user = models.OneToOneField(User, related_name = 'profile', on_delete = models.CASCADE)
	is_online = models.BooleanField(default = False)

	def __str__(self):
		return self.user.username

class UserImage(models.Model):
	user = models.OneToOneField(User, related_name = 'userimage', on_delete = models.CASCADE)
	avatar = models.ImageField(upload_to='images/', blank = True, null = True, default = 'images/avatar.png')

	def __str__(self):
		return self.user.username
