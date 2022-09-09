from django.urls import path
from Dealer import views

urlpatterns = [

	# Home 
	path('<slug:ref>/', views.home, name="dealerHome"), 
	path('inventory-chart/', views.inventory_chart, name='inventory-chart'),
	
	# Customer List 
	path('dealerCustomerList/<slug:ref>/', views.dealerCustomerList, name="dealerCustomerList"),
	path('dealerAddCustomer/<slug:ref>/', views.dealerAddCustomer, name='dealerAddCustomer'),
	path('dealerDeleteCustomer/<slug:ref>/<data_id>', views.dealerDeleteCustomer, name="dealerDeleteCustomer"),
	
	# Inventory List 
	path('dealerInventoryList/<slug:ref>/', views.dealerInventoryList, name="dealerInventoryList"),
	path('dealerAddInventory/<slug:ref>/', views.dealerAddInventory, name='dealerAddInventory'),
	path('dealerDeleteInventory/<slug:ref>/<data_id>', views.dealerDeleteInventory, name="dealerDeleteInventory"),
	
	# Order Queue
	path('dealerOrderQueue/<slug:ref>/', views.dealerOrderQueue, name="dealerOrderQueue"),
	path('dealerOrderQueueInsert/<slug:ref>/', views.dealerOrderQueueInsert, name="dealerOrderQueueInsert"),
	path('dealerDeleteOrderQueue/<slug:ref>/<data_id>', views.dealerDeleteOrderQueue, name="dealerDeleteOrderQueue"),
	
	
	# path('orderQueue-chart/', views.order_queue_chart, name='orderQueue-chart'),
]