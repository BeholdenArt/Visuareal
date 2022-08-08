from django.shortcuts import render, redirect
from Company.models import AddCustomer, AddCompany, CompanyInventory
from Dealer.models import AddDealer
from django.contrib.auth.decorators import login_required
from Influencer.models import AddInfluencer
from django.http import HttpResponse
from Users.models import User
# Create your views here.


def home(request, ref=''):
	if ref: 
		user = User.objects.get(referrelCode= ref)
		if user is not None: 
			context = {
				'url' : 'influencer',
				'user': user,
				'ref': ref
			}
			return render(request, 'base.html', context)

	else:
		return redirect('login')

def customerList(request, ref):
	if ref: 
		user = User.objects.get(referrelCode= ref) 
		if user is not None: 
			return HttpResponse("CUSTOMER LIST ENTERED")
	else:
		return redirect('login')
	# contents = AddCustomer.objects.all()
	# context = {
	# 	'all_data' : contents, 
	# 	'extend' : 'base.html', 
	# 	'url' : "influencer", 
	# 	'name': "Influencer's",
	# }
	# return render(request, '<>/customerlist.html', context)

def addCustomer(request):
	if request.method == "POST": 
		name = request.POST["name"]
		pnumber = request.POST["pnumber"]
		influencedThrough = request.POST.get("influencedThrough")
		interestedCompany = request.POST.get("interesetdCompany")
		interestedProduct = request.POST.get("interestedProduct")
		dealerSuggested = request.POST.get("dealerSuggested")
		dealerName = AddDealer.objects.filter(dealerName__exact = dealerSuggested)
		# print(type(dealerSuggested))
		obj = AddCustomer(
				customerName= name, customerPhoneNumber= pnumber, 
				influencedThrough= influencedThrough, 
				companyInterested= interestedCompany,
				interestedProduct= interestedProduct, 
				dealerName = dealerName[0],
			)
		obj.save()
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