from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.contrib.auth.decorators import login_required



# Signup Function
def signup(request):

    if request.method == "POST":

        department_name = request.POST['department_name']
        email = request.POST['email']
        department_id = request.POST['department_id']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']


        # Check email already exists
        if Department.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')


        # Password match check
        if password != confirm_password:
            messages.error(request, "Password does not match!")
            return redirect('signup')


        Department.objects.create(
            department_name=department_name,
            email=email,
            department_id=department_id,
            password=password
        )


        messages.success(request, "Signup successful! Please login.")
        return redirect('login')


    return render(request,'signup.html')





# Login Function
def login(request):

    if request.method == "POST":

        department_id = request.POST['department_id']
        password = request.POST['password']


        try:
            department = Department.objects.get(
                department_id=department_id,
                password=password
            )

            # session create
            request.session['department_id'] = department.department_id

            return redirect('dashboard')


        except Department.DoesNotExist:
            messages.error(request, "Invalid ID or Password")
            return redirect('login')


    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def assigned_complaints(request):
    return render(request, 'assigned_complaints.html')

def report(request):
    return render(request, 'report.html')

def profile(request):
    return render(request, 'profile.html')

def notification(request):
    return render(request, 'notification.html')

def resolved_complaints(request):
    return render(request, 'resolved_complaints.html')

def update_status(request):
    return render(request, 'update_status.html')