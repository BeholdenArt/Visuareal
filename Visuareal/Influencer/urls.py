from django.urls import path
from Influencer import views

urlpatterns = [
	path('<slug:ref>', views.home, name="home"), 
	path('', views.home, name='home'), 
	path('customerList/<slug:ref>', views.customerList, name='customerList'), 
	path('addCustomer/', views.addCustomer, name='addCustomer'), 

]