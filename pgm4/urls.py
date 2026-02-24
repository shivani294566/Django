from django.urls import path
from pgm4.views import home,contacts,aboutus
urlpatterns=[
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('aboutus/', aboutus, name='aboutus'),
]