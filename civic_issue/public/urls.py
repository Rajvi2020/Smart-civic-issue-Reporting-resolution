from django.urls import path
from public import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('features/', views.features),
    path('contact/', views.contact),
]
