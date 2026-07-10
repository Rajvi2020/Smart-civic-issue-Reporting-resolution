from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')

def contact(request):
    return render(request, 'contact.html')

def contact(request):

    if request.method == "POST":

        name = request.POST['name']

        email = request.POST['email']

        message = request.POST['message']


        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )


        return redirect('/contact/')


    return render(request,'contact.html')