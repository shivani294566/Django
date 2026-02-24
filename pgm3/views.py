from django.shortcuts import render
from .models import Student

# Create your views here.
def display_lists(request):
    fruits=["Apple","Banana","Orange","Grapes"]
    students=["John","James","Smith","Jacob"]
    return render(request,'pgm3/display_list.html',{'fruits':fruits, 'students':students})