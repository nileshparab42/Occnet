from django.shortcuts import render

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
    return render(request,'contact-us.html')


