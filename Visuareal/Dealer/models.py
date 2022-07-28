from django.db import models
from Company.models import Inventory
# Create your models here.


# Create your models here.
class UserCredentials(models.Model):
	username = models.CharField(max_length= 10)
	email = models.EmailField()
	password = models.CharField(max_length=20)

	class Meta: 
		abstract = True

class UserDocuments(models.Model):
	panNumber = models.CharField(max_length= 30)
	panPhoto = models.ImageField(upload_to='PanCard/')

	class Meta: 
		abstract = True

class DealerInventory(Inventory): 
	dealer = models.ForeignKey('Dealer.AddDealer', on_delete= models.CASCADE, blank= True)

class AddDealer(UserCredentials, UserDocuments):
	dealerName = models.CharField(max_length= 255)
	points = models.IntegerField()			# POINT MODULE REMAINING
	referrelCode = models.CharField(max_length= 20, unique= True)
	UserDocuments._meta.get_field('panPhoto').upload_to = 'PanCard/Dealer/'
	
	def __str__(self):
		return str(self.dealerName)