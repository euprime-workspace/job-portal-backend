from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from . import views

<<<<<<< HEAD
urlpatterns=[
    path("Profile/",views.ProfileView.as_view(),name="Create_Profile"),

    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
=======
urlpatterns = [
    path("create_Profile/", views.CreateProfile, name="Create_Profile"),
    path("signup/", views.signUp, name="signup"),
    path("login/", views.login, name="login"),
]
>>>>>>> 54770beb9351841cba7474185b754a5fe65525af
