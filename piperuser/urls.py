from django.urls import path
from piperuser import views 

urlpatterns = [
	path('', views.profile, name = 'profile'),
	path('register/', views.register, name = 'register'),
	path('profile/edit/', views.editprofile, name = 'editprofile'),
	path('profile/password/', views.changepassword, name = 'changepassword'),
	path('profile/search/', views.profilesearch, name = 'profilesearch'),
	path('upload/image/', views.imageupload, name = 'userimage'),
]