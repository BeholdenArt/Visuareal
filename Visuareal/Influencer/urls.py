from django.urls import path
from Influencer import views

urlpatterns = [
	path('', views.home, name="home"), 
]