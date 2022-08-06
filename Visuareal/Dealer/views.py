from django.shortcuts import render
from Dealer.models import DealerInventory 
from Company.models import AddCustomer, OrderQueue
from django.http import HttpResponse
import json 
from django.http import JsonResponse
from django.core import serializers
from json import dumps
# Create your views here.



def home(request):
	context = {
		'extend': 'base.html', 
		 'url' : "dealer", 
		 'name': "Dealer's", 
	}
	return render(request, 'home.html', context)

def inventory_chart(request):
    labels = []
    data = []

    queryset = DealerInventory.objects.values('productName', 'productQuantity')
    for entry in queryset:
        labels.append(entry['productName'])
        data.append(entry['productQuantity'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


    

def customerList(request):
	contents = AddCustomer.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : "dealer", 
		 'name': "Dealer's", 
	}
	return render(request, 'customerlist.html', context)

def dealerInventory(request):
	contents = DealerInventory.objects.all()
	context = {
		'all_data' : contents,
		'extend' : 'base.html', 
		'url' : "dealer", 
		 'name': "Dealer's",  
	}
	return render(request, 'inventorylist.html', context)

def orderQueue(request):
	contents = OrderQueue.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : "dealer", 
		 'name': "Dealer's", 
	}
	return render(request, 'orderqueue.html', context)