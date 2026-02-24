from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    return HttpResponse("Program1")
def current_datetime(request):
    now=datetime.datetime.now()
    html1="<h1>Current date and time is %s</h1>\n" %now
    dt=datetime.datetime.now()+datetime.timedelta(hours=4)
    html2="<h1>In 4 hours, it will be %s</h1>" %dt
    dt=datetime.datetime.now()-datetime.timedelta(hours=4)
    html3="<h1>Before 4 hours, it was %s</h1>" %dt
    return HttpResponse(html1+'\n'+html2+'\n'+html3) 
