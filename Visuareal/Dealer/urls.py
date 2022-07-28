from django.urls import path
from Dealer import views

urlpatterns = [
	path('', views.home, name="home"), 
]