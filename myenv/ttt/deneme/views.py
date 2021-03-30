from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def student(request):
    return render(request, 'accounts/student.html')

def teacher(request):
    return render(request, 'accounts/teacher.html')

def manager(request):
    return render(request, 'accounts/manager.html')

