from django.shortcuts import render,redirect
from Candidate.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, "index.html")


def job(request):
    return render(request, "job.html")


def prejob(request):
    return render(request, "job.html")


def infojob(request):
    return render(request, "job-info.html")

#name= sandesh pass= 8qP7WCctv5s6PT7
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("http://127.0.0.1:8000/")
        else:
            return render(request, "job.html")
    return render(request, "log-in.html")

def signuppage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        qualification = request.POST.get("qualification")
        password = request.POST.get("password")
        try :
           user =User.objects.create_user(username=username,email=email,last_name=qualification,password=password)
           login(request,user)
           return redirect("http://127.0.0.1:8000/")
        except  :
            messages.error(request,  "Username already exist !")
            return render(request, "sign-up.html")
    return render(request, "sign-up.html")

def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(
            name=name, email=email, message=message, time=datetime.today()
        )
        contact.save()
        messages.success(request, "Your message has been sent !")
    return render(request, "contact-us.html")


def logoutpage(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/")

def aboutus(request):
    return render(request,"about-us.html")