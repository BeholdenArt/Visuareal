from django.urls import path
from Dealer import views

urlpatterns = [
	path('', views.home, name="home"), 
	path('customerList/', views.customerList, name="customerList"),
	path('inventoryList/', views.dealerInventory, name="inventoryList"),
	path('addInventory/', views.addInventory, name='addInventory'),
	path('deleteInventory/<data_id>', views.deleteInventory, name="deleteInventory"),
	path('orderQueue/', views.orderQueue, name="orderQueue"),
	path('orderQueueInsert/', views.addOrderQueue, name="orederQueueInsert"),
	path('deleteOrderQueue/<data_id>', views.deleteOrderQueue, name="deleteOrderQueue"),
	path('addCustomer/', views.addCustomer, name='addCustomer'),
	path('deleteCustomer/<data_id>', views.deleteCustomer, name="deleteCustomer"),
]