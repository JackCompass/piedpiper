from django.shortcuts import render, HttpResponse, redirect, reverse
from piperuser.forms import Registration, EditProfileForm, ImageForm
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from asgiref.sync import sync_to_async
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
		'flag' : False
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
def imageupload(request):
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES, instance = request.user.userimage)
		if form.is_valid():
			form.save()
			return redirect(reverse('profile'))
		else:
			return render(request, 'piperuser/upload.html', {
				'form' : form,
			})

	else:
		form = ImageForm(instance = request.user.userimage)
		return render(request, 'piperuser/upload.html', {
			'form' : form,
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
				'flag' : True,
			})
			
	else:
		return render(request, 'piperuser/searchuser.html')
