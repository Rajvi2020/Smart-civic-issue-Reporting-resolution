from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Citizen, Complaint,Feedback




def home(request):

    return render(
        request,
        "citizen/home.html"
    )





def register_view(request):

    if request.method == "POST":


        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]


        password1 = request.POST["password1"]
        password2 = request.POST["password2"]


        mobile = request.POST["mobile"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        pincode = request.POST["pincode"]




        if password1 != password2:

            return render(
                request,
                "citizen/register.html",
                {
                    "error":"Password not match"
                }
            )




        if User.objects.filter(username=username).exists():

            return render(
                request,
                "citizen/register.html",
                {
                    "error":"Username already exists"
                }
            )




        user = User.objects.create_user(

            username=username,

            first_name=first_name,

            last_name=last_name,

            email=email,

            password=password1

        )




        Citizen.objects.create(

            user=user,

            mobile=mobile,

            address=address,

            city=city,

            state=state,

            pincode=pincode

        )



        return redirect("login")




    return render(
        request,
        "citizen/register.html"
    )







def login_view(request):

    if request.method == "POST":


        username = request.POST["username"]

        password = request.POST["password"]




        user = authenticate(

            request,

            username=username,

            password=password

        )




        if user is not None:


            login(request,user)

            return redirect("dashboard")



        else:


            return render(
                request,
                "citizen/login.html",
                {
                    "error":"Invalid username or password"
                }
            )




    return render(
        request,
        "citizen/login.html"
    )







from django.shortcuts import get_object_or_404


@login_required
def dashboard(request):

    citizen = get_object_or_404(
        Citizen,
        user=request.user
    )


    return render(
        request,
        "citizen/dashboard.html",
        {
            "citizen": citizen
        }
    )


    citizen = Citizen.objects.get(
        user=request.user
    )


    return render(
        request,
        "citizen/dashboard.html",
        {
            "citizen": citizen
        }
    )

@login_required
@login_required
def report_issue(request):


    citizen = Citizen.objects.get(
        user=request.user
    )


    if request.method == "POST":


        title = request.POST["title"]

        department = request.POST["department"]

        description = request.POST["description"]

        location = request.POST["location"]

        image = request.FILES.get("image")



        Complaint.objects.create(

            citizen=citizen,

            title=title,

            department=department,

            description=description,

            location=location,

            image=image

        )


        return redirect("dashboard")



    return render(
        request,
        "citizen/report_issue.html"
    )


    citizen = Citizen.objects.get(
        user=request.user
    )


    if request.method == "POST":


        title = request.POST["title"]

        category = request.POST["category"]

        description = request.POST["description"]

        location = request.POST["location"]

        image = request.FILES.get("image")



        Complaint.objects.create(

            citizen=citizen,

            title=title,

            category=category,

            description=description,

            location=location,

            image=image

        )



        return redirect("dashboard")



    return render(
        request,
        "citizen/report_issue.html"
    )


@login_required
def my_complaints(request):


    citizen = Citizen.objects.get(
        user=request.user
    )


    complaints = Complaint.objects.filter(
        citizen=citizen
    ).order_by("-created_at")



    return render(
        request,
        "citizen/my_complaints.html",
        {
            "complaints": complaints
        }
    )
@login_required
def track_status(request):


    citizen = Citizen.objects.get(
        user=request.user
    )


    complaints = Complaint.objects.filter(
        citizen=citizen
    ).order_by("-created_at")



    return render(
        request,
        "citizen/track_status.html",
        {
            "complaints": complaints
        }
    )
@login_required
def public_complaints(request):


    complaints = Complaint.objects.all().order_by("-created_at")


    return render(
        request,
        "citizen/public_complaints.html",
        {
            "complaints": complaints
        }
    )


    complaints = Complaint.objects.all().order_by("-created_at")


    return render(
        request,
        "citizen/public_complaints.html",
        {
            "complaints": complaints
        }
    )
@login_required
def upvote_issue(request, id):


    complaint = Complaint.objects.get(
        id=id
    )


    if request.user in complaint.upvotes.all():

        complaint.upvotes.remove(
            request.user
        )


    else:

        complaint.upvotes.add(
            request.user
        )


    return redirect("public_complaints")
@login_required
def give_feedback(request, id):


    complaint = Complaint.objects.get(
        id=id
    )


    citizen = Citizen.objects.get(
        user=request.user
    )



    if request.method == "POST":


        rating = request.POST["rating"]

        message = request.POST["message"]



        Feedback.objects.create(

            complaint=complaint,

            citizen=citizen,

            rating=rating,

            message=message

        )



        return redirect(
            "my_complaints"
        )



    return render(
        request,
        "citizen/feedback.html",
        {
            "complaint": complaint
        }
    )
@login_required
def profile_view(request):

    citizen = Citizen.objects.get(
        user=request.user
    )


    return render(
        request,
        "citizen/profile.html",
        {
            "citizen": citizen
        }
    )
def logout_view(request):

    logout(request)

    return redirect("login")