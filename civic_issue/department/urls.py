from django.urls import path
from . import views


urlpatterns = [

    path(
        'signup/',
        views.signup,
        name='signup'
    ),

    path(
        'login/',
        views.login,
        name='login'
    ),
    path(
        'dashboard/',
        views.dashboard,name='dashboard'
    ),
    path(
        'assigned-complaints/',
        views.assigned_complaints,
        name='assigned_complaints'
    ),
    path(
        'report/',
        views.report,
        name='report'
    ),
    path(
        'profile/',
        views.profile,
        name='profile'
    ),
    path(
        'notification/',
        views.notification,
        name='notification'
    ),
    path(
        'resolved_complaints/',
        views.resolved_complaints,
        name='resolved_complaints'
    ),
    path(
        'update_status/',
        views.update_status,
        name='update_status'
    )
]
