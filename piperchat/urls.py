from django.urls import path
from piperchat import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('edit_profile/', views.profile_edit, name = 'profile_edit')
]