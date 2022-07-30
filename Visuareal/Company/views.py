from django.shortcuts import render
from django.http import HttpResponse
from Company.models import AddCustomer, CompanyInventory, OrderQueue, AddCompany
from Dealer.models import AddDealer
from Influencer.models import AddInfluencer

# Create your views here.

def home(request):
	return render(request, 'base.html')

def customerList(request):

	contents = AddCustomer.objects.all()
	# print(contents[0].interestedProduct.all())
	return render(request, 'customerlist.html', {'all_data' : contents})

def companyInventory(request):
	contents = CompanyInventory.objects.all()
	return render(request, 'inventorylist.html', {'all_data' : contents})

def dealerList(request):
	contents = AddDealer.objects.all()
	return render(request, 'dealerlist.html', {'all_data' : contents}) 

def influencerList(request):
	contents = AddInfluencer.objects.all()
	return render(request, 'influencerlist.html', {'all_data' : contents})

def orderQueue(request):
	contents = OrderQueue.objects.all()
	return render(request, 'orderqueue.html', {'all_data' : contents})