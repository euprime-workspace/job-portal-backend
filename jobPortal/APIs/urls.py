from django.urls import path

from . import views

urlpatterns = [
    path("create_Profile/", views.CreateProfile.as_view(), name="Create_Profile"),
    path("signup/", views.signUp, name="signup"),
    path("login/", views.login, name="login"),
]
