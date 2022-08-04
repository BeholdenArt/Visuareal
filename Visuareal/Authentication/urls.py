from django.urls import path
from Authentication import views

urlpatterns = [
	path('login', views.home, name='home'), 
	path('signup', views.signup, name='signup'), 
]