from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile,File

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

    def create(self, validated_data):
        # Create a File instance and associate it with the 'resume' field
        uploaded_file = self.context['request'].data.get('resume')
        if uploaded_file:
            file_instance = File(uploaded_file=uploaded_file)
            file_instance.save()
            validated_data['resume'] = file_instance

        profile = super().create(validated_data)
        return profile