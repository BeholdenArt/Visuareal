from django.db import models

# Create your models here.
class UserCredentials(models.Model):
    username = models.CharField(max_length= 30, verbose_name= "Username")
    email = models.EmailField(null= True, blank= True, verbose_name= "Email")
    password = models.CharField(max_length=20, verbose_name= "Password")

    class Meta: 
    	abstract = True

class UserDocuments(models.Model):
    panNumber = models.CharField(max_length= 30, verbose_name= "Pan Number")
    panPhoto = models.ImageField(verbose_name= "Pan Photo")

    def __str__(self):
    	return str(self.panNumber)

    class Meta: 
    	abstract = True

class Inventory(models.Model):
	productName = models.CharField(max_length= 255, verbose_name= "Product Name")
	productCategory = models.CharField(max_length= 255, verbose_name= "Product Category")
	productQuantity = models.CharField(max_length= 255, verbose_name= "Product Quantity")

	def __str__(self):
		return str(self.productName)

	class Meta: 
		abstract = True

class Points(models.Model):
	totalPoint = models.IntegerField(default= 0, verbose_name= "Total Point")
	createdOn = models.DateTimeField(auto_now_add = True, verbose_name= "Created On")
	updatedOn = models.DateTimeField(auto_now= True, verbose_name= "Last Updated")

	def __str__(self):
		return str(self.totalPoint)

	class Meta: 
		abstract = True

class OrderQueue(models.Model):
	orderedProducts = models.ManyToManyField('Company.CompanyInventory', verbose_name= "Order Placed", blank= True)
	orderFrom = models.ForeignKey('Dealer.AddDealer', on_delete= models.CASCADE, verbose_name= "Dealer Who Ordered")
	orderTo = models.ForeignKey('Company.AddCompany', on_delete= models.CASCADE, verbose_name= "Company Whom Ordered")
	placedOn = models.DateTimeField(blank= True, null= True)
	expectedDelievery = models.DateTimeField(blank= True, null= True)

	def __str__(self):
		return str(self.orderFrom)

class AddCustomer(models.Model):
	customerName = models.CharField(max_length= 30, verbose_name= "Customer Name")
	customerPhoneNumber = models.BigIntegerField(verbose_name= "Phone Number")
	interestedProduct = models.ManyToManyField('Company.CompanyInventory', blank= True, verbose_name= "Interested Product")
	companyInterested = models.ForeignKey('Company.AddCompany', on_delete = models.CASCADE, blank= True, null= True, verbose_name= "Interested Company")
	influencedThrough = models.ForeignKey('Influencer.AddInfluencer', on_delete= models.CASCADE, blank= True, null= True, verbose_name= "Influencer (if any)")
	dealerName = models.ForeignKey('Dealer.AddDealer', on_delete= models.CASCADE, blank= True, null= True, verbose_name= "Dealer Name")
	createdOn = models.DateTimeField(auto_now_add= True, verbose_name= "Created On")
	updatedOn = models.DateTimeField(auto_now = True, verbose_name= "Last Updated")

	def __str__(self):
		return str(self.customerName)

class CompanyInventory(Inventory):
	companyName = models.ForeignKey('Company.AddCompany', on_delete= models.CASCADE, blank= True)

class AddCompany(models.Model):
	companyName = models.CharField(max_length= 30, verbose_name= "Company Name")
	dealerList = models.ManyToManyField('Dealer.AddDealer', blank= True, verbose_name= "Dealer List")
	influencerList = models.ManyToManyField('Influencer.AddInfluencer', blank= True, verbose_name= "Influencer List") 

	def __str__(self):
		return str(self.companyName)