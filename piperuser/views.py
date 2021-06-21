from django.shortcuts import render, HttpResponse

def register(request):
	return render(request, 'piperuser/register.html')
	

