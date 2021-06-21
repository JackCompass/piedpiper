from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

@login_required()
# @cache_control(no_cache = True, must_revalidate = True)
def home(request):
	username = request.user.username
	name = 'Anuj Singh'
	profession = 'Student'
	return render(request, 'piperchat/chat.html', {
		'username' : username,
		'name' : name,
		'profession' : profession
	})

@login_required()
def profile_edit(request):
	return render(request, 'piperchat/edit.html')
