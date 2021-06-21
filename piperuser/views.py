from django.shortcuts import render, HttpResponse, redirect, reverse
from piperuser.forms import Registration, EditProfileForm
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
	# When the POST request comes we have to validate the data.
	if (request.method == 'POST'):
		form = Registration(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Account Created')
		else:
			return render(request, 'piperuser/register.html', {
				'form' : form
			})
	form = Registration()
	return render(request, 'piperuser/register.html', {
		'form' : form,
	})
	
@login_required
def profile(request):
	return render(request, 'piperuser/profile.html', {
		'user' : request.user,
	})

@login_required
def editprofile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect(reverse('profile'))
	else:
		form = EditProfileForm(instance = request.user)
		return render(request, 'piperuser/editprofile.html', {
			'form' : form
		})

def changepassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data = request.POST, user = request.user)
		if form.is_valid():
			form.save()
			return redirect(reverse('profile'))
		else:
			return render(request, 'piperuser/password.html', {
				'form' : form
			})
	else:
		form = PasswordChangeForm(user = request.user)
		return render(request, 'piperuser/password.html', {
			'form' : form
		})