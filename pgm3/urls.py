from django.urls import path
from pgm3.views import display_lists
urlpatterns=[
    path("", display_lists),

]