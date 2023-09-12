from django.shortcuts import render, redirect
from django.http import HttpResponse


# Import any models or forms you may have here

def index(request):
    return render(request, "home.html")

def admin_registration(request):
    return render(request, "admin_registration.html")

def admin_login(request):
    return render(request, "admin_login.html")

def lectures_seminar(request):
    return render(request, "lectures_seminar.html")


def studentevents(request):
    return render(request, "studentevents.html")

def liveevents(request):
    return render(request, "liveevents.html")

def requestform(request):
    return render(request, "requestform.html")

def registration(request):
    return render(request, 'admin_registration.html')

def dashboard(request):
    return render(request,"dashboard.html")

