from django.urls import path
from Company import views

urlpatterns = [
	path('', views.home, name="home"), 
	path('customerList/', views.customerList, name="customerList"),
	path('inventoryList/', views.companyInventory, name="inventoryList"),
	path('dealerList/', views.dealerList, name="dealerList"),  
	path('influencerList/', views.influencerList, name="influencerList"), 
	path('orderQueue/', views.orderQueue, name="orderQueue"),
	path('addCustomer/', views.addCustomer, name='addCustomer'),
	path('deleteCustomer/<data_id>', views.deleteCustomer, name="deleteCustomer"),
	path('addInventory/', views.addInventory, name='addInventory'),
	path('deleteCompanyInventory/<data_id>', views.deleteInventory, name="deleteCompanyInventory"),
	path('orderQueueInsert/', views.addOrderQueue, name="orederQueueInsert"),
	path('deleteOrderQueue/<data_id>', views.deleteOrderQueue, name="deleteOrderQueue"),
	path('company-inventory-chart', views.inventory_chart, name='company-inventory-chart'),
]