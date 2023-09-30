from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Profile
from .serializers import ProfileSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

class ProfileView(generics.ListCreateAPIView):
    serializer_class=ProfileSerializer
    queryset=Profile.objects.all()
