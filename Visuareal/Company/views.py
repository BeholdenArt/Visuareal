from django.shortcuts import render, redirect
from Company.models import AddCustomer, CompanyInventory, OrderQueue, AddCompany
from Dealer.models import AddDealer
from Influencer.models import AddInfluencer
from django.http import HttpResponse


def home(request):
	context = {
		'url' : 'company', 
		'name' : "Company's",
	}	
	return render(request, 'base.html', context)

def customerList(request):
	contents = AddCustomer.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : 'company', 
		'name' : "Company's",
	}
	return render(request, 'company/customerlist.html', context)


def companyInventory(request):
	contents = CompanyInventory.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : 'company',
		'name' : "Company's",
	}	
	return render(request, 'company/inventorylist.html', context)

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
	return render(request, 'company/orderqueue.html', context)

def addInventory(request):
	if request.method == "POST":
		ProductName = request.POST["ProductName"]
		ProductCategory = request.POST["ProductCategory"]
		ProductQuantity = request.POST["ProductQuantity"]
		companyName = request.POST.get("CompanyName")
		company = AddCompany.objects.filter(companyName__exact = companyName)
		obj = CompanyInventory(
			productName = ProductName,
			productCategory = ProductCategory,
			productQuantity = ProductQuantity,
			companyName = company[0]
		)
		obj.save()
		return HttpResponse("Added, You may close this window now")
	else:
		CompanyName = AddCompany.objects.all()
		context = {
			'CompanyName' : CompanyName,
			'extend' : 'popup.html',
		}
		return render(request, 'company/inventoryInsert.html', context)

def deleteInventory(request, data_id):
	event = CompanyInventory.objects.get(pk=data_id)
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
		return render(request, 'company/orderQueueInsert.html', context)

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
		return render(request, 'company/customerListInsert.html', context)

def deleteCustomer(request, data_id):
	event = AddCustomer.objects.get(pk=data_id)
	event.delete()
	return redirect('../customerList')