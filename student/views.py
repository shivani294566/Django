from django.shortcuts import render
from student.models import *

# Create your views here.
def registrationform(request):
	msg=""
	if request.method=="POST":
		sd=RegistrationForm()
		sd.name=request.POST["name"] 
		sd.emailid=request.POST["emailid"] 
		sd.password=request.POST["password"] 
		sd.mobilenumber=request.POST["mobilenumber"] 
		sd.pincode=request.POST["pincode"] 
		sd.city=request.POST["city"] 
		sd.save()
		msg="Registered Successfully"
	return render(request,"registrationform.html",{"msg":msg})

def client(request):
	msg=""
	if request.method=="POST":
		sd=Client()
		sd.drivername=request.POST["drivername"]
		sd.vehiclename=request.POST["vehiclename"]
		sd.vehicletype=request.POST["vehicletype"]
		sd.modelyear=request.POST["modelyear"]
		sd.drivermobilenumber=request.POST["drivermobilenumber"]
		sd.drivinglicencenumber=request.POST["drivinglicencenumber"]
		sd.rateperkilometer=request.POST["rateperkilometer"]
		sd.city=request.POST["city"]
		sd.save()
		msg="Registered Successfully"
	return render(request,"client.html",{"msg":msg})

def registeredusers(request):
	msg=""
	data=""
	if request.method=="POST":
		sid=request.POST["sid"]
		RegistrationForm.objects.filter(id=sid).delete()
		msg="Record Deleted Successfully"
	data=RegistrationForm.objects.all()	
	return render(request,"Registeredusers.html",{"data":data,"msg":msg})

def searchoperation(request):
	data=""
	msg=""
	operation=""
	if request.method=="POST":
		operation=request.POST["btnsubmit"]
		
		if operation=="x":
			sid=request.POST["sid"]
			RegistrationForm.objects.filter(id=sid).delete()
			msg="Record Deleted"
		else:
			searchby=int(request.POST["searchby"])
			value=request.POST["value"]
			if searchby==1:
				data=RegistrationForm.objects.filter(name=value)
			elif searchby==2:
				data=RegistrationForm.objects.filter(emailid=value)
			elif searchby==3:
				data=RegistrationForm.objects.filter(mobilenumber=value)
			elif searchby==4:
				data=RegistrationForm.objects.filter(pincode=value)
			elif searchby==5:
				data=RegistrationForm.objects.filter(city=value)
			if data.exists():
				pass;
			else:
				msg="Record Not Found"
	return render(request,"searchoperation.html",{"data":data,"msg":msg})
def login(request):
	msg=""
	if request.method=="POST":
		p_mobilenumber=request.POST["mobilenumber"]
		p_password=request.POST["password"]
		if RegistrationForm.objects.filter(mobilenumber=p_mobilenumber,password=p_password).exists():
			request.session["mobilenumber"]=p_mobilenumber
		return render(request,"studenthome.html")
	else: 
		msg="Invalid Login Details"
	return render(request,"login.html",{"msg":msg})

def clientdisplay(request):
	msg=""
	
	if request.method=="POST":
		sid=request.POST["sid"]
		Client.objects.filter(id=sid).delete()
		msg="Record Seleted Sucessfully"
	data=Client.objects.all()
	return render(request,"clientdisplay.html",{"data":data,"msg":msg})



def changepassword(request):
	msg=""
	if request.method=="POST":
		currentpassword=request.POST["currentpassword"]
		newpassword=request.POST["newpassword"]
		confirmnewpassword=request.POST["confirmnewpassword"]
		p_mobilenumber=request.session["mobilenumber"]
		if newpassword==confirmnewpassword:
			if RegistrationForm.objects.filter(mobilenumber=p_mobilenumber,password=currentpassword).exists():
				RegistrationForm.objects.filter(mobilenumber=p_mobilenumber,password=currentpassword).update(password=newpassword)
				msg="password change Successfully"
			else:
				msg="New password & Confirm New Password must match"
	return render(request,"changepassword.html",{"msg":msg})

def clientsearch(request):
	data=""
	msg=""
	if request.method=="POST":
		operation=request.POST["btnsubmit"]
		if operation=="x":
			sid=request.POST["sid"]
			Customer.objects.filter(id=sid).delete()
			msg="Record Deleted"
		else:
			searchby=int(request.POST["Searchby"])
			value=request.POST["value"]
			if searchby==1:
				data=Client.objects.filter(drivername__contains=value)
			elif searchby==2:
				data=Client.objects.filter(vehiclename__contains=value)
			elif searchby==3:
				data=Client.objects.filter(vehicletype__contains=value)
			elif searchby==4:
				data=Client.objects.filter(modelyear=value)
			elif searchby==5:
				data=Client.objects.filter(drivermobilenumber=value)
			elif searchby==6:
				data=Client.objects.filter(drivinglicencenumber=value)
			elif searchby==7:
				data=Client.objects.filter(city__contains=value)
			elif data.exists():
				pass;
			else:
				msg="Record Not Found"
	return render(request,"clientsearch.html",{"data":data,"msg":msg})
    
def studenthome(request):
    return render(request,"studenthome.html")

    		

    	
    	
    	
    	





	       














	    



	