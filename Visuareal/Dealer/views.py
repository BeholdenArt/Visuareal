from django.shortcuts import render
from Dealer.models import DealerInventory 
from Company.models import AddCustomer, OrderQueue
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Dealer.models import AddDealer
# Create your views here.

context = {}

@login_required(login_url= "login")
def home(request):
	global context
	context['url'] = 'dealer'
	context['name'] = "Dealer's" 
	return render(request, 'base.html', context)
 
@login_required(login_url= "login")
def customerList(request):
	global context
	contents = AddCustomer.objects.all()
	context['all_data']= contents
	return render(request, 'customerlist.html', context)


@login_required(login_url= "login")
def dealerInventory(request):
	global context
	contents = DealerInventory.objects.all()
	context['all_data']= contents
	return render(request, 'inventorylist.html', context)

@login_required(login_url= "login")
def orderQueue(request):
	global context
	contents = OrderQueue.objects.all()
	context['all_data']= contents
	return render(request, 'orderqueue.html', context)

@login_required(login_url= "login")
def addDealerInventory(request):
	global context
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
		context['all_data']= contents

		return render(request, 'inventoryListInsert.html', context)

# def addorderQueue(request):
# 	if request.method == "POST":
