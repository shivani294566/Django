from django.shortcuts import render,HttpResponse
import csv
from reportlab.pdfgen import canvas
from .models import Student

# Create your views here.
def export_students_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename=students.csv'
    writer=csv.writer(response)
    writer.writerow(['Name'])
    students=Student.objects.all().values_list('name')
    for student in students:
        writer.writerow(student)

    return response
def export_students_pdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] ='attachment;filename=students.pdf'

    v=canvas.Canvas(response)
    students=Student.objects.all()
    y=800
    for student in students:
        v.drawString(100,y,"student name:{student.name}")
        y-=40

        v.showPage()
        v.save()
        return response   
