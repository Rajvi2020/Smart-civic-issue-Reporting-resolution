from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            admin = AdminLogin.objects.get(
                email=email,
                password=password
            )

            return redirect("admin_dashboard")

        except AdminLogin.DoesNotExist:
            return render(request, "login.html", {
                "error": "Invalid Email or Password"
            })

    return render(request, "login.html")