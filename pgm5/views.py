from django.shortcuts import render,redirect
from .models import Course, Student
from django.urls import reverse
# Create your views here.
def register_student(request):
    if request.method=='POST':
        student_name=request.POST.get('student_name')
        course_id=request.POST.get('course_id')
        student=Student.objects.create(name=student_name)
        course=Course.objects.get(id=course_id)
        return(redirect(reverse(course_detail, args=(course_id, ))))
    courses=Course.objects.all()
    return render(request, 'pgm5/register_student.html',{'courses':courses})
def course_detail(request, course_id):
    course=Course.objects.get(id=course_id)
    students=Course.students.all()
    return render(request, 'pgm5/course_detail.html',{'course':course,'students':students})
