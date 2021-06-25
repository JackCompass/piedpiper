from django.shortcuts import render, HttpResponse, redirect, reverse
from piperuser.forms import Registration, EditProfileForm
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from asgiref.sync import sync_to_async
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from piperuser.models import Profile

def register(request):
	'''It registers new users into the database'''
	# When the POST request comes we have to validate the data.
	if (request.method == 'POST'):
		form = Registration(request.POST)
		if form.is_valid():
			new_user = form.save()
			Profile.objects.create(user = new_user)
			new_user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'],)
			login(request, new_user)
			return redirect(reverse('profile'))
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

@login_required
def profilesearch(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		try:
			searched_user = User.objects.get(username = username)
		except User.DoesNotExist:
			return render(request, "piperuser/notfound.html")
		else:
			print(searched_user.is_active)
			print(searched_user.username)
			print(searched_user.first_name)
			return render(request, 'piperuser/profile.html', {
				'user' : searched_user,
				'username' : searched_user.username,
			})
			
	else:
		return render(request, 'piperuser/searchuser.html')

@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):    
	user.profile.is_online = True
	user.profile.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):   
	user.profile.is_online = False
	user.profile.save()
