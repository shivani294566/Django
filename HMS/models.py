from django.db import models

class EmployeeData(models.Model):
	employeeid=models.CharField(max_length=100)
	fullname=models.CharField(max_length=100)
	gender=models.CharField(max_length=100)
	dateofbirth=models.CharField(max_length=13)
	contactnumber=models.CharField(max_length=100)
	emailid=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	softdelete=models.IntegerField(default=0)
	createdon=models.CharField(max_length=100)
	deletedon=models.CharField(max_length=100,default="")


