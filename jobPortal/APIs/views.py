from django.shortcuts import render
from rest_framework import generics

from .models import Profile
from .serializers import ProfileSerializer

class CreateProfile(generics.CreateAPIView):
    serializer_class=ProfileSerializer
    queryset=Profile.objects.all()