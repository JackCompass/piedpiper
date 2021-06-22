from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

@login_required()
# @cache_control(no_cache = True, must_revalidate = True)
def index(request):
	return render(request, 'piperchat/index.html')


@login_required()
def room(request, room_name):
	return render(request, 'piperchat/room.html', {
		'room_name' : room_name,
	})

