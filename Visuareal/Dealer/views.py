from django.shortcuts import render
from Dealer.models import DealerInventory 
from Company.models import AddCustomer, OrderQueue, CompanyInventory, AddCompany
from django.shortcuts import redirect
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
		return render(request, 'inventoryInsert.html', context)

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
		return render(request, 'orderQueueInsert.html', context)

def deleteOrderQueue(request, data_id):
	event = OrderQueue.objects.get(pk=data_id)
	event.delete()
	return redirect('../orderQueue')