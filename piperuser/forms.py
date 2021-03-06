from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from captcha.fields import CaptchaField
from django import forms 
from piperuser.models import UserImage
from django.contrib.auth.models import User

class Registration(UserCreationForm):
	captcha = CaptchaField()

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'captcha')

	def __init__(self, *args, **kwargs):
		super(Registration, self).__init__(*args, **kwargs)
		self.fields['captcha'].widget.attrs['style'] = 'width:105px;height: 33px'

class EditProfileForm(UserChangeForm):
	captcha = CaptchaField()

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'captcha')

	def __init__(self, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.fields['captcha'].widget.attrs['style'] = 'width:105px;height: 33px'


class ImageForm(forms.ModelForm):
	class Meta:
		model = UserImage
		fields = ('avatar', )