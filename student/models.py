from django.db import models

# Create your models here.
class RegistrationForm(models.Model):
	name=models.CharField(max_length=15,default="")
	emailid=models.CharField(max_length=100,default="")
	password=models.CharField(max_length=10,default="")
	mobilenumber=models.CharField(max_length=10,default="")
	pincode=models.CharField(max_length=10,default="")
	city=models.CharField(max_length=20,default="")

class Client(models.Model):
	drivername=models.CharField(max_length=20,default="")
	emailid=models.CharField(max_length=100,default="")
	vehiclename=models.CharField(max_length=20,default="")
	vehicletype=models.CharField(max_length=300,default="")
	modelyear=models.CharField(max_length=10,default="")
	drivermobilenumber=models.CharField(max_length=10,default="")
	drivinglicencenumber=models.CharField(max_length=20,default="")
	rateperkilometer=models.CharField(max_length=10,default="")
	city=models.CharField(max_length=10,default="")