from django.urls import path
from adminapp import views

urlpatterns = [
    path('login/', views.login,name="admin_login"),
    path('admin_dashboard/', views.admin_dashboard,name="admin_dashboard"),
]