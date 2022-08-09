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
		return render(request, 'companyinventoryInsert.html', context)

def deleteInventory(request, data_id):
	event = CompanyInventory.objects.get(pk=data_id)
	event.delete()
	return redirect (request, '../inventoryList')