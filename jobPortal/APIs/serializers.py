from rest_framework import serializers
from django.core.files.base import ContentFile

from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    fileInput = serializers.FileField(write_only=True)  # This field will handle the file upload

    class Meta:
        model = Profile
        exclude = ['resume']

    def create(self, validated_data):
        # Get the file data from the serializer
        file_data = validated_data.pop('fileInput', None)
        print(file_data)
        # Create the File instance and save the file data to it
        if file_data:
            file_instance = File.objects.create()
            file_instance.uploaded_file.save(file_data.name, ContentFile(file_data.read()))
            validated_data['resume'] = file_instance  # Associate the File instance with the 'resume' field

        # Create the Profile instance without the 'resume' field
        profile = Profile.objects.create(**validated_data)

        return profile

    def __str__(self):
        return self.user.username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __str__(self):
        return self.username
