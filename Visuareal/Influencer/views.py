from django.shortcuts import render
from Company.models import AddCustomer, AddCompany, CompanyInventory
from Dealer.models import AddDealer
from Influencer.models import AddInfluencer
from django.http import HttpResponse
# Create your views here.


def home(request):
	context = {
		'url' : 'influencer',
		'name': "Influencer's",
	}
	return render(request, 'base.html', context)

def customerList(request):
	contents = AddCustomer.objects.all()
	context = {
		'all_data' : contents, 
		'extend' : 'base.html', 
		'url' : "influencer", 
		'name': "Influencer's",
	}
	return render(request, 'customerlist.html', context)

def addCustomer(request):
	if request.method == "POST": 
		name = request.POST["name"]
		pnumber = request.POST["pnumber"]
		influencedThrough = request.POST.get("influencedThrough")
		interestedCompany = request.POST.get("interesetdCompany")
		interestedProduct = request.POST.get("interestedProduct")
		dealerSuggested = request.POST.get("dealerSuggested")
		# print(type(dealerSuggested))
		obj = AddCustomer(
				customerName= name, customerPhoneNumber= pnumber, 
				influencedThrough= influencedThrough, 
				companyInterested= interestedCompany,
				interestedProduct= interestedProduct, 
				dealerName = dealerSuggested
			)
		print(obj)
		return HttpResponse("VALUE INSERTED")

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
		return render(request, 'customerListInsert.html', context)