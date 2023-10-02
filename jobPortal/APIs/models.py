from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

from simple_history.models import HistoricalRecords


class File(models.Model):
    uploaded_file = models.FileField(upload_to="uploads/")
    history = HistoricalRecords()

    def __str__(self):
        return self.uploaded_file.name


class CustomUser(models.Model):
    userTypes=(
        ("Recruiter","Recruiter"),
        ("Candidate","Candidate")
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    user_type=models.CharField(max_length=9,choices=userTypes)

    def __str__(self):
        return self.username
    
class Recruiter(models.Model):
    firstname= models.CharField(max_length=25)
    lastname= models.CharField(max_length=25)
    company= models.CharField(max_length=50)
    email= models.EmailField()
    phone=models.CharField(max_length=15)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="recruitor")

    def __str__(self):
        return self.company

class Profile(models.Model):
    roles = (
        ('SDE Backend', 'SDE Backend'),
        ('SDE Frontend', 'SDE Frontend'),
        ('Data Analyst', 'Data Analyst'),
        ('Data Scientist', 'Data Scientist'),
        ('Machine Learning Engineer', 'Machine Learning Engineer'),
        ('Machine Learning Scientist', 'Machine Learning Scientist')
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    last_login_time = models.DateTimeField(default=timezone.now)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    resume = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, related_name='profile_file')
    academic_Record = models.TextField(null=True)
    internship_exp = models.TextField(null=True)
    research_exp = models.TextField(null=True)
    role = models.CharField(max_length=45, choices=roles)

    def __str__(self):
        return self.user.username
