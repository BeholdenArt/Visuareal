from django.shortcuts import render
from Company.models import AddCustomer
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
