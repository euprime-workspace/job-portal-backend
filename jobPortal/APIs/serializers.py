from rest_framework import serializers

from .models import *

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        fields=['uploaded_file']
    
    def __str__(self):
        return self.uploaded_file.name

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['last_login_time','id']

    def __str__(self):
        return self.user.username
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=['username','password','user_type']

    def __str__(self):
        return self.username
    
class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=['username','user_type']

    def __str__(self):
        return self.username
    
class ProfileViewSerializer(serializers.ModelSerializer):
    resume = FileSerializer()
    user=UserViewSerializer()
    class Meta:
        model=Profile
        fields='__all__'

    def __str__(self):
            return self.user.username
    
class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        exclude=['id']

    def __str__(self):
        return self.company

class RecruiterViewSerializer(serializers.ModelSerializer):
    user=UserViewSerializer()
    class Meta:
        model = Recruiter
        fields='__all__'

    def __str__(self):
        return self.company
    
class JobDescriptionSerializer(serializers.ModelSerializer):
    company_docs = serializers.FileField(required=False)
    username=models.CharField(max_length=45)
    class Meta:
        model=JobDescription
        exclude=['updated_at','created_at','id']

    def __str__(self):
        return self.company_name.company