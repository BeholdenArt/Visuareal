from django.urls import path
from Company import views

urlpatterns = [
	# Home 
	path('<slug:ref>/', views.home, name="companyHome"), 
	path('company-inventory-chart', views.inventory_chart, name='company-inventory-chart'),
	
	# Customer list
	path('companyCustomerList/<slug:ref>/', views.companyCustomerList, name="companyCustomerList"),
	path('companyAddCustomer/<slug:ref>/', views.companyAddCustomer, name='companyAddCustomer'),
	path('companyDeleteCustomer/<slug:ref>/<data_id>', views.companyDeleteCustomer, name="companyDeleteCustomer"),
	
	# Influencer List
	path('companyInfluencerList/<slug:ref>/', views.companyInfluencerList, name="companyInfluencerList"), 
	path('companyDeleteInfluencer/<slug:ref>/<data_id>', views.companyDeleteInfluencer, name="companyDeleteInfluencer"), 

	# Dealer List	
	path('companyDealerList/<slug:ref>/', views.companyDealerList, name="companyDealerList"),  
	path('companyDeleteDealer/<slug:ref>/<data_id>', views.companyDeleteDealer, name="companyDeleteDealer"),
	
	# Inventory List
	path('companyInventoryList/<slug:ref>/', views.companyInventoryList, name="companyInventoryList"),
	path('companyAddInventory/<slug:ref>/', views.companyAddInventory, name='companyAddInventory'),
	path('companyDeleteInventory/<slug:ref>/<data_id>', views.companyDeleteInventory, name="companyDeleteInventory"),

	# Order Queue
	path('companyOrderQueue/<slug:ref>/', views.companyOrderQueue, name="companyOrderQueue"),
	path('companyOrderQueueInsert/<slug:ref>/', views.companyOrderQueueInsert, name="companyOrderQueueInsert"),
	path('companyDeleteOrderQueue/<slug:ref>/<data_id>', views.companyDeleteOrderQueue, name="companyDeleteOrderQueue"),
	path('companyapproveOrderQueue/<slug:ref>/<data_id>', views.companyapproveOrderQueue, name="companyapproveOrderQueue"),
	
	#Extra Points
	path('companyExtraPoints/<slug:ref>/', views.extraPoints, name="companyExtraPoints"),
	path('updateExtraPoints/<slug:ref>/<data_id>', views.updateExtraPoints, name="updateExtraPoints"),
	
]