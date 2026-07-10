from django.db import models
from django.contrib.auth.models import User



class Citizen(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    mobile = models.CharField(
        max_length=15,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    state = models.CharField(
        max_length=100,
        blank=True
    )

    pincode = models.CharField(
        max_length=10,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.user.username





class Complaint(models.Model):


    STATUS_CHOICES = [

        ("Pending","Pending"),

        ("In Progress","In Progress"),

        ("Resolved","Resolved"),

    ]



    citizen = models.ForeignKey(
        Citizen,
        on_delete=models.CASCADE
    )



    title = models.CharField(
        max_length=200
    )



    department = models.CharField(
        max_length=100
    )



    description = models.TextField()



    location = models.CharField(
        max_length=200
    )



    image = models.ImageField(
        upload_to="complaints/",
        blank=True,
        null=True
    )



    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    upvotes = models.ManyToManyField(
        User,
        related_name="upvoted_complaints",
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Feedback(models.Model):

    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name="feedbacks"
    )


    citizen = models.ForeignKey(
        Citizen,
        on_delete=models.CASCADE
    )


    rating = models.IntegerField(
        default=5
    )


    message = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )



    def __str__(self):

        return self.complaint.title
    def __str__(self):

        return self.title