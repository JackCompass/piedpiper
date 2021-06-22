from django.urls import path
from piperchat import views
from piperuser import views as v

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<str:room_name>/', views.room, name = 'room')
	# path('edit_profile/', views.profile_edit, name = 'profile_edit')
]