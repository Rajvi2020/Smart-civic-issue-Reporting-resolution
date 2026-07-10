from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),          # 👈 Home Page
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("report-issue/", views.report_issue, name="report_issue"),
    path(
    "my-complaints/",
    views.my_complaints,
    name="my_complaints"
),
path(
    "track-status/",
    views.track_status,
    name="track_status"
),
path(
    "issues/",
    views.public_complaints,
    name="public_complaints"
),


path(
    "upvote/<int:id>/",
    views.upvote_issue,
    name="upvote_issue"
),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.logout_view, name="logout"),
    path(
    "feedback/<int:id>/",
    views.give_feedback,
    name="give_feedback"
),
]
