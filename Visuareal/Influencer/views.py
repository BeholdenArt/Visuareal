from django.shortcuts import render
from Company.models import AddCustomer, AddCompany, CompanyInventory
from Dealer.models import AddDealer
from Influencer.models import AddInfluencer
from django.http import HttpResponse
# Create your views here.


def home(request):
	cont = AddCustomer.objects.count()
	contents = AddCustomer.objects.all().order_by('-id')[:5]
	context = {
		'all_data' : contents,
		'customer' : cont,
		'url' : 'influencer',
		'name': "Influencer's",
		'extend' : "base.html"
	}
	return render(request, 'influencerhome.html', context)

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
		return render(request, 'customerListInsert.html', context)