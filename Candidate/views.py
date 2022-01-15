from django.shortcuts import render
from Candidate.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def job(request):
    return render(request,'job.html')

def prejob(request):
    return render(request,'prejob.html')

def infojob(request):
    return render(request,'job-info.html')

def contactus(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name,email=email,message=message,time=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent !')
    return render(request,'contact-us.html')


