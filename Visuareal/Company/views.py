from django.shortcuts import render
from Company.models import AddCustomer, CompanyInventory, OrderQueue, AddCompany
from Dealer.models import AddDealer
from Influencer.models import AddInfluencer
from django.http import JsonResponse
from django.http import HttpResponse
import json 

def home(request):
	context = {
		'url' : 'company', 
		'name' : "Company's",
		'extend' : "base.html" ,
	}	
	return render(request, 'CuHome.html', context)

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