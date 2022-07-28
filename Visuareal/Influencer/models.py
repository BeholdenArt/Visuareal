from django.db import models
from Dealer.models import UserCredentials, UserDocuments
# Create your models here.


class AddInfluencer(UserDocuments, UserCredentials):
	influencerName = models.CharField(max_length= 30)
	points = models.IntegerField()			# POINT MODULE REMAINING
	referrelCode = models.CharField(max_length= 40, unique= True)
	UserDocuments._meta.get_field('panPhoto').upload_to = 'PanCard/Influencer/'
	
	def __str__(self):
		return str(self.influencerName)