from django.urls import path
from piperuser import views 

urlpatterns = [
	path('', views.register, name = 'register'),
]