from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pgm4/home.html')
def contacts(request):
    return render(request, 'pgm4/contacts.html')
def aboutus(request):
    return render(request, 'pgm4/aboutus.html')