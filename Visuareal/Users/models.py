from django.db import models
from django.contrib.auth.models import AbstractUser
from Users.manager import UserManager
# Create your models here.

class User(AbstractUser):
	username = None 
	email = models.EmailField(unique= True)
	phoneNumber = models.BigIntegerField(null= True, blank= True, verbose_name= 'Phone Number')
	gstinNumber = models.CharField(max_length= 60, default='', blank= True, verbose_name='GSTIN Number')
	referrelCode = models.CharField(max_length= 20, default='', blank= True, verbose_name= "Referrel Code")
	panNumber = models.CharField(max_length= 30, default='', blank= True, verbose_name= "Pan Number")
	panPhoto = models.ImageField(blank= True, verbose_name= "Pan Photo")

	objects = UserManager() 

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = [] 