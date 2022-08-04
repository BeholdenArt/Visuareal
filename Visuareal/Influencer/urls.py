from django.urls import path
from Influencer import views

urlpatterns = [
	path('', views.home, name="home"), 
	path('customerList/', views.customerList, name='customerList'), 
	path('addCustomer/', views.addCustomer, name='addCustomer'), 
]