from rest_framework import serializers
from django.contrib.auth.models import User

<<<<<<< HEAD
from .models import Profile,File
=======
from .models import *

>>>>>>> 54770beb9351841cba7474185b754a5fe65525af

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

<<<<<<< HEAD
    def create(self, validated_data):
        # Create a File instance and associate it with the 'resume' field
        uploaded_file = self.context['request'].data.get('resume')
        if uploaded_file:
            file_instance = File(uploaded_file=uploaded_file)
            file_instance.save()
            validated_data['resume'] = file_instance

        profile = super().create(validated_data)
        return profile
=======
    def __str__(self):
        return self.user.username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __str__(self):
        return self.username
>>>>>>> 54770beb9351841cba7474185b754a5fe65525af
