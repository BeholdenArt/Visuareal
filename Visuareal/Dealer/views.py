from django.shortcuts import render
from Dealer.models import DealerInventory 
from Company.models import AddCustomer, OrderQueue
from django.http import HttpResponse

from Dealer.models import AddDealer
# Create your views here.



def home(request):
	context = {
		 'url' : "dealer", 
		 'name': "Dealer's", 
	}
	return render(request, 'base.html', context)

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

def addDealerInventory(request):
	if request.method == "POST":
		ProductName = request.POST["ProductName"]
		ProductCategory = request.POST["ProductCategory"]
		ProductQuantity = request.POST["ProductQuantity"]
		DName = request.POST.get("DealerName")
		d = AddDealer.objects.filter(dealerName__exact = DName)
		obj = DealerInventory(
			productName = ProductName,
			productCategory = ProductCategory,
			productQuantity = ProductQuantity,
			dealer = d[0],
		)
		obj.save()
		return HttpResponse("ITS ALIVE")
	else:
		DealerName = AddDealer.objects.all()
		context = {
			'DealerName' : DealerName,
			'extend' : 'popup.html',
		}
		return render(request, 'inventoryListInsert.html', context)

# def addorderQueue(request):
# 	if request.method == "POST":
