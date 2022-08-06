from django.db import models
from Dealer.models import UserCredentials, UserDocuments, Points
# Create your models here.


class AddInfluencer(UserDocuments, UserCredentials, Points):
	influencerName = models.CharField(max_length= 30, verbose_name="Influencer Name")
	referrelCode = models.CharField(max_length= 40, unique= True, verbose_name= "Referrel Code")
	UserDocuments._meta.get_field('panPhoto').upload_to = 'PanCard/Influencer/'
	
	def __str__(self):
		return str(self.influencerName)