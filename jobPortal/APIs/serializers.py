from rest_framework import serializers
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer

from .models import *

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    class Meta:
        model=CustomUser

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    class Meta:
        model=CustomUser

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        exclude=['history']
    
    def __str__(self):
        return self.uploaded_file.name

class ProfileSerializer(serializers.ModelSerializer):
    fileInput = serializers.FileField(max_length=100000,allow_empty_file=False)  # This field will handle the file upload

    class Meta:
        model = Profile
        exclude = ['resume']

    def create(self, validated_data):
        # Get the file data from the serializer
        file_data = validated_data.pop('fileInput', None)
        print(file_data)
        # Create the File instance and save the file data to it
        if file_data:
            file_serializer=FileSerializer(data=file_data)
            if file_serializer.is_valid():
                print("valid")
                file_serializer.save()

        # Create the Profile instance without the 'resume' field
        profile = Profile.objects.create(**validated_data)

        return profile

    def __str__(self):
        return self.user.username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude=['id']

    def __str__(self):
        return self.username
    
class RecruiterSerializer(serializers.ModelSerializer):
    username=models.CharField(max_length=45)
    class Meta:
        model = Recruiter
        exclude=['user']
    
    def create(self, validated_data):
        user=validated_data.pop('username',None)
        validated_data['user']=CustomUser.objects.get(username=user)
        recruiter=Recruiter.objects.create(**validated_data)

        return recruiter

    def __str__(self):
        return self.company
