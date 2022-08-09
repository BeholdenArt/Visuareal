from django.urls import path
from Company import views
from Influencer import views as Influ_views

urlpatterns = [
	path('', views.home, name="home"), 
	path('customerList/', views.customerList, name="customerList"),
	path('inventoryList/', views.companyInventory, name="inventoryList"),
	path('dealerList/', views.dealerList, name="dealerList"),  
	path('influencerList/', views.influencerList, name="influencerList"), 
	path('orderQueue/', views.orderQueue, name="orderQueue"),
	path('addCustomer/', Influ_views.addCustomer, name='addCustomer'),
	path('deleteCustomer/<data_id>', Influ_views.deleteCustomer, name="deleteCustomer"),
	path('addInventory/', views.addInventory, name='addcompanyInventory'),
	path('deleteInventory/<data_id>', views.deleteInventory, name="deletecompanyInventory"),
]