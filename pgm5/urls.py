from django.urls import path
from .views import register_student, course_detail

urlpatterns=[
    path('register_student/', register_student, name='register_student'),
    path('course_detail/<int:course_id/', course_detail, name='course_detail'),
]