from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Citizen


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "mobile",
        "city",
        "state",
        "created_at"
    )