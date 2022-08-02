from django.shortcuts import render
from Dealer.models import DealerInventory 
from Company.models import AddCustomer, OrderQueue
from django.http import HttpResponse
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