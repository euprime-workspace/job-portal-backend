from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

    def __str__(self):
        return self.user.username