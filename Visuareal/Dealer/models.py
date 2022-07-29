from django.db import models
from Company.models import Inventory, Points, UserDocuments, UserCredentials
# Create your models here.


# Create your models here.

class DealerInventory(Inventory): 
	dealer = models.ForeignKey('Dealer.AddDealer', on_delete= models.CASCADE, blank= True)

class AddDealer(UserCredentials, UserDocuments, Points):
	dealerName = models.CharField(max_length= 255, verbose_name= "Dealer Name")
	referrelCode = models.CharField(max_length= 20, unique= True, verbose_name= "Referrel Code")
	UserDocuments._meta.get_field('panPhoto').upload_to = 'PanCard/Dealer/'
	
	def __str__(self):
		return str(self.dealerName)