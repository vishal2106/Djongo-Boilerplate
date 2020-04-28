from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student

def home(request):
    student_data = Student.objects.all()
    for field  in student_data:
        print("Name of the student is:", field.name)
    return HttpResponse("See the terminal for response")