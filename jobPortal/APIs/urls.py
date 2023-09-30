from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from . import views

urlpatterns=[
    path("Profile/",views.ProfileView.as_view(),name="Create_Profile"),

    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]