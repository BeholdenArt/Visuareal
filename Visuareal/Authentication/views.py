from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
		'name': 'Authentication', 
		'url': 'authentication', 
		'extend': 'base.html', 
	}
	return render(request, 'Authentication/login.html', context)

def signup(request):
	context = {
		'name': 'Authentication', 
		'url' : 'authentication', 
		'extend' : 'base.html', 
	}
	return render(request, 'Authentication/signup.html', context)