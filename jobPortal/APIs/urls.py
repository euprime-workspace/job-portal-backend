from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path("create_Profile/", views.CreateProfile, name="Create_Profile"),
    path("signup/", views.signUp, name="signup"),
    path("login/", views.login, name="login"),
    path("googleLogin/", views.googleLogin, name="googleLogin"),

    path("recruiter/create/", views.createRecruiter, name="Create_Recruiter"),
    path("recruiter/view/", views.viewRecruiter, name="View_Recruiter"),
    path("candidate/all/", views.viewCandidates, name="viewAllProfiles"),
    path("candidate/<uuid:id>/", views.viewCandidateProfile, name="viewCandidateProfile"),
    path("candidate/<uuid:id>/<str:question>/", views.askQuery, name="askCandidateProfile"),
    path("getUserId/", views.getUserId, name="getUserId"),

    path("jobs/",views.viewJobs,name="jobs"),
    path("job/<str:id>/",views.viewJobDescription,name="job_description"),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
