from django.shortcuts import render
from Company.models import AddCustomer, CompanyInventory, OrderQueue, AddCompany
from Dealer.models import AddDealer
from Influencer.models import AddInfluencer
from django.http import JsonResponse
from django.http import HttpResponse
import json 
from django.core import serializers


def home(request):
	contents = AddCustomer.objects.count()
	inventory = CompanyInventory.objects.count()
	order = OrderQueue.objects.count()
	context = {
		'customer' : contents,
		'inventory' : inventory,
		'order' : order,
		'url' : 'company', 
		'name' : "Company's",
		'extend' : "base.html" ,
	}
	return render(request, 'CompanyHome.html', context)

def inventory_chart(request):
	labels = []
	data = []

	queryset = CompanyInventory.objects.values('productName', 'productQuantity')
	for entry in queryset:
		labels.append(entry['productName'])
		data.append(entry['productQuantity'])
	
	return JsonResponse(data={
		'labels': labels,
		'data': data,
	})

# def order_queue_chart(request):
# 	labels2 = []
# 	data2 = []

# 	queryset = OrderQueue.objects.values('orderedQuantity')
# 	queryset2 = OrderQueue.objects.all()
# 	query = []
# 	for i in queryset2:
# 		a = i.orderedProducts.values('productName')
# 		print(a)
# 	print(queryset, query)
# 	for entry in queryset:
# 		data2.append(entry['orderedQuantity'])
# 	print(data2)
# 	print(labels2)
# 	return JsonResponse(data={
# 		'labels2': labels2,
# 		'data2': data2,
# 	})


def customerList(request):
	contents = AddCustomer.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : 'company', 
		'name' : "Company's",
	}
	return render(request, 'customerlist.html', context)

def companyInventory(request):
	contents = CompanyInventory.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : 'company', 
		'name' : "Company's",
	}	
	return render(request, 'inventorylist.html', context)

def dealerList(request):
	contents = AddDealer.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html',	
		'url' : 'company', 
		'name' : "Company's",
	}
	return render(request, 'dealerlist.html', context) 

def influencerList(request):
	contents = AddInfluencer.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html',
		'url' : 'company',
		'name' : "Company's", 
	}
	return render(request, 'influencerlist.html', context)

def orderQueue(request):
	contents = OrderQueue.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : 'company', 
		'name' : "Company's",
	}
	return render(request, 'orderqueue.html', context)