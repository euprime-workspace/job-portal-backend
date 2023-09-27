from django.urls import path

from . import views

urlpatterns=[
    path("create_Profile/",views.CreateProfile.as_view(),name="Create_Profile")
]