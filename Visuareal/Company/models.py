from django.db import models

# Create your models here.
class UserCredentials(models.Model):
    username = models.CharField(max_length= 30)
    email = models.EmailField(null= True, blank= True)
    password = models.CharField(max_length=20)

    class Meta: 
    	abstract = True

class UserDocuments(models.Model):
    panNumber = models.CharField(max_length= 30)
    panPhoto = models.ImageField()

    class Meta: 
    	abstract = True

class Inventory(models.Model):
	productName = models.CharField(max_length= 255)
	productCategory = models.CharField(max_length= 255)
	productQuantity = models.CharField(max_length= 255)

	class Meta: 
		abstract = True

class AddCustomer(models.Model):
	customerName = models.CharField(max_length= 30)
	customerPhoneNumber = models.BigIntegerField()
	interestedProduct = models.ManyToManyField('Company.CompanyInventory', blank= True)
	companyInterested = models.ForeignKey('Company.AddCompany', on_delete = models.CASCADE, blank= True, null= True)
	influencedThrough = models.ForeignKey('Influencer.AddInfluencer', on_delete= models.CASCADE, blank= True, null= True)
	dealerName = models.ForeignKey('Dealer.AddDealer', on_delete= models.CASCADE, blank= True, null= True)
	createdOn = models.DateTimeField(auto_now_add= True)
	updatedOn = models.DateTimeField(auto_now = True)

	def __str__(self):
		return str(self.customerName)

class CompanyInventory(Inventory):
	companyName = models.ForeignKey('Company.AddCompany', on_delete= models.CASCADE, blank= True)

class AddCompany(models.Model):
	companyName = models.CharField(max_length= 30)
	dealerList = models.ManyToManyField('Dealer.AddDealer', blank= True)
	influencerList = models.ManyToManyField('Influencer.AddInfluencer', blank= True) 

	def __str__(self):
		return str(self.companyName)