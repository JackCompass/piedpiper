from django.urls import path
from piperuser import views 

urlpatterns = [
	path('', views.register, name = 'register'),
	path('profile/', views.profile, name = 'profile'),
	path('profile/edit/', views.editprofile, name = 'editprofile'),
	path('profile/password/', views.changepassword, name = 'changepassword')
]