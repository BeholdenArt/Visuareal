from django.urls import path
from Dealer import views

urlpatterns = [
	path('', views.home, name="home"), 
	path('customerList/', views.customerList, name="customerList"),
	path('inventoryList/', views.dealerInventory, name="inventoryList"),
	path('addDealerInventory/', views.addDealerInventory, name='addDealerInventory'),
	path('orderQueue/', views.orderQueue, name="orderQueue"),
	path('inventory-chart/', views.inventory_chart, name='inventory-chart'),
	# path('orderQueue-chart/', views.order_queue_chart, name='orderQueue-chart'),
	path('orderQueueInsert/', views.addOrderQueue, name="orederQueueInsert"),
]