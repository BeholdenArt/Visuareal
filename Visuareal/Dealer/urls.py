from django.urls import path
from Dealer import views
from Influencer import views as Influ_views

urlpatterns = [
	path('', views.home, name="home"), 
	path('customerList/', views.customerList, name="customerList"),
	path('inventoryList/', views.dealerInventory, name="inventoryList"),
	path('addInventory/', views.addInventory, name='adddealerInventory'),
	path('deleteInventory/<data_id>', views.deleteInventory, name="deletedealerInventory"),
	path('orderQueue/', views.orderQueue, name="orderQueue"),
	path('orderQueueInsert/', views.addOrderQueue, name="orederQueueInsert"),
	path('deleteOrderQueue/<data_id>', views.deleteOrderQueue, name="deleteOrderQueue"),
	path('addCustomer/', Influ_views.addCustomer, name='addCustomer'),
	path('deleteCustomer/<data_id>', Influ_views.deleteCustomer, name="deleteCustomer"),
]