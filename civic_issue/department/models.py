from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):

    department_name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    department_id = models.CharField(
        max_length=50,
        unique=True
    )

    password = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        db_table = "departments"


    def __str__(self):
        return self.department_name

class Complaint(models.Model):

    STATUS_CHOICES = (
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Resolved','Resolved'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.CharField(max_length=100)

    description = models.TextField()

    location = models.CharField(max_length=200)

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigned_complaints"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )


    def __str__(self):
        return self.category