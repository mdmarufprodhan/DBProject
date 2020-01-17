from django.http import HttpResponse
from django.shortcuts import render

from B1.models import Student


def home(request):
    return render(request, 'home.html')


def showStudent(request):

    allStudents = Student.objects.all()
  #  print(allStudents)

    context = { "allStudents" : allStudents }

    return render(request, 'student.html', context)

