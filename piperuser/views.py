from django.shortcuts import render, HttpResponse
from piperuser.forms import Registration

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
	

