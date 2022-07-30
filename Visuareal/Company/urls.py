from django.urls import path
from Company import views

urlpatterns = [
	path('', views.home, name="home"), 
	path('customerList/', views.customerList, name="customerList"),
	path('inventoryList/', views.companyInventory, name="inventoryList"),
	path('dealerList/', views.dealerList, name="dealerList"),  
	path('influencerList/', views.influencerList, name="influencerList"), 
	path('orderQueue/', views.orderQueue, name="orderQueue"),
]