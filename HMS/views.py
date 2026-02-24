from django.shortcuts import render
from HMS.models import *
from datetime import datetime

def searchemployee(request):
	msg=""
	empdata=""
	if request.method=="POST":
		empname=request.POST.get("fullname","")
		if(request.POST.get("btndelete","")):
			empid=request.POST.get("empid","0")
			EmployeeData.objects.filter(id=empid,softdelete=0).update(softdelete=1,deletedon=datetime.now().strftime("%d-%m-%Y %I-%M %p"))
			msg="Record Deleted"
		else:
			if EmployeeData.objects.filter(fullname__icontains=empname,softdelete=0).exists():
				empdata=EmployeeData.objects.filter(fullname__icontains=empname,softdelete=0)
			else:
				msg="Record not found"
	return render(request,"searchemployee.html",{"msg":msg,"empdata":empdata})


def employee_registration(request):
	msg=""
	if request.method=="POST":
		if EmployeeData.objects.filter(employeeid=request.POST.get("employeeid",""),softdelete=0).exists():
			msg="Employee ID already exists"
		else:
			ed=EmployeeData()
			ed.employeeid=request.POST.get("employeeid","")
			ed.fullname=request.POST.get("fullname","")
			ed.gender=request.POST.get("gender","")
			ed.dateofbirth=request.POST.get("dateofbirth","")
			ed.contactnumber=request.POST.get("contactnumber","")
			ed.emailid=request.POST.get("emailid","")
			ed.address=request.POST.get("address","")
			ed.createdon=datetime.now().strftime("%d-%m-%Y %I-%M %p")
			ed.save()
			msg="Register successfully"
	return render(request,"employee_registration.html",{"msg":msg})

