from django.shortcuts import render, redirect
from Dealer.models import DealerInventory 
from Company.models import AddCustomer, OrderQueue, CompanyInventory, AddCompany
from Influencer.models import AddInfluencer
from django.shortcuts import redirect
from django.http import HttpResponse

from Dealer.models import AddDealer
from django.http import HttpResponse
import json 
from django.http import JsonResponse
from django.core import serializers
from json import dumps
# Create your views here.

def home(request):
	contents = AddCustomer.objects.count()
	inventory = DealerInventory.objects.count()
	order = OrderQueue.objects.count()
	context = {
		'customer' : contents,
		'inventory' : inventory,
		'order' : order,
		'extend': 'base.html', 
		 'url' : "dealer", 
		 'name': "Dealer's", 
	}
	return render(request, 'dealerhome.html', context)

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

# def order_queue_chart(request):
#     labels2 = []
#     data2 = []

#     queryset = OrderQueue.objects.values('orderedProducts', 'orderedQuantity')
#     for entry in queryset:
#         labels2.append(entry['orderedProducts'])
#         data2.append(entry['orderedQuantity'])
    
#     return JsonResponse(data={
#         'labels2': labels2,
#         'data2': data2,
#     })


def customerList(request):
	contents = AddCustomer.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : "dealer", 
		 'name': "Dealer's", 
	}
	return render(request, 'dealer/customerlist.html', context)

def dealerInventory(request):
	contents = DealerInventory.objects.all()
	context = {
		'all_data' : contents,
		'extend' : 'base.html', 
		'url' : "dealer", 
		 'name': "Dealer's",  
	}
	return render(request, 'dealer/inventorylist.html', context)

def orderQueue(request):
	contents = OrderQueue.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : "dealer", 
		 'name': "Dealer's", 
	}
	return render(request, 'dealer/orderqueue.html', context)

def addInventory(request):
	if request.method == "POST":
		ProductName = request.POST["ProductName"]
		ProductCategory = request.POST["ProductCategory"]
		ProductQuantity = request.POST["ProductQuantity"]
		DName = request.POST.get("DealerName")
		dealer = AddDealer.objects.filter(dealerName__exact = DName)
		obj = DealerInventory(
			productName = ProductName,
			productCategory = ProductCategory,
			productQuantity = ProductQuantity,
			dealer = dealer[0],
		)
		obj.save()
		return HttpResponse("Added, You may close this window now")
	else:
		DealerName = AddDealer.objects.all()
		context = {
			'DealerName' : DealerName,
			'extend' : 'popup.html',
		}
		return render(request, 'dealer/inventoryInsert.html', context)

def deleteInventory(request, data_id):
	event = DealerInventory.objects.get(pk=data_id)
	event.delete()
	return redirect ('../inventoryList')


def addOrderQueue(request):
	if request.method == "POST":
		PN = request.POST.get("ProductName")
		productSelected = CompanyInventory.objects.exclude(productName = PN)
		OP = request.POST.get("OrderPlaced")
		OT = request.POST.get("Companywhomordered")
		OrderPlaced = AddDealer.objects.filter(dealerName__exact = OP)
		OrderTo = AddCompany.objects.filter(companyName__exact = OT)
		orderedQuantity = request.POST["orderedQuantity"]
		Placedon = request.POST["Placedon"]
		Expecteddeliveryon = request.POST["Expecteddeliveryon"]
		obj = OrderQueue.objects.create(
			orderFrom = OrderPlaced[0],
			orderTo = OrderTo[0],
			orderedQuantity = orderedQuantity,
			placedOn = Placedon,
			expectedDelievery = Expecteddeliveryon,
		)
		for pdt in productSelected:
			obj.orderedProducts.add(pdt)

		obj.save()
		print(obj)
		return HttpResponse("Added, You may close this window now")

	else:
		ProductName = CompanyInventory.objects.all()
		OrderPlaced = AddDealer.objects.all()
		OrderTo = AddCompany.objects.all()
		context = {
			'ProductName' : ProductName,
			'OrderPlaced' : OrderPlaced,
			'Companywhomordered' : OrderTo,
			'extend' : 'popup.html',
		}
		return render(request, 'dealer/orderQueueInsert.html', context)

def deleteOrderQueue(request, data_id):
	event = OrderQueue.objects.get(pk=data_id)
	event.delete()
	return redirect('../orderQueue')

def addCustomer(request):
	if request.method == "POST": 
		name = request.POST["name"]
		pnumber = request.POST["pnumber"]
		influencedThrough = request.POST.get("influencedThrough")
		interestedCompany = request.POST.get("interestedCompany")
		interestedPdt = request.POST.get("interestedProducts")
		dealerSuggested = request.POST.get("dealerSuggested")
		dealerName = AddDealer.objects.filter(dealerName__exact = dealerSuggested)
		companyInterested = AddCompany.objects.filter(companyName__exact = interestedCompany)
		influenced = AddInfluencer.objects.filter(influencerName__exact = influencedThrough)
		productInterested = CompanyInventory.objects.exclude(productName = interestedPdt)
		obj = AddCustomer.objects.create(
				customerName= name, customerPhoneNumber= pnumber, 
				influencedThrough= influenced[0],
				companyInterested= companyInterested[0],
				dealerName = dealerName[0],
			)
		for pdt in productInterested:
			obj.interestedProduct.add(pdt)
		obj.save()
		return HttpResponse("Added You may close this window now")


	else:
		dealerList = AddDealer.objects.all() 
		influencerList = AddInfluencer.objects.all() 
		companyList = AddCompany.objects.all() 
		companyInventory = CompanyInventory.objects.all()
		context = {
			'dealerList' : dealerList,
			'influencerList' : influencerList,
			'companyList' : companyList, 
			'companyInventory' : companyInventory, 
			'extend' : 'popup.html',  
		}
		return render(request, 'dealer/customerListInsert.html', context)

def deleteCustomer(request, data_id):
	event = AddCustomer.objects.get(pk=data_id)
	event.delete()
	return redirect('../customerList')