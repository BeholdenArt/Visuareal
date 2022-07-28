from django.urls import path
from Company import views

urlpatterns = [
	path('', views.home, name="home"), 
]