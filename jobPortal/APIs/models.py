from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from simple_history.models import HistoricalRecords

class File(models.Model):
    uploaded_file=models.FileField(upload_to="uploads/")
    history=HistoricalRecords()

class Profile(models.Model):
    roles=(
        ('SDE Backend','SDE Backend'),
        ('SDE Frontend','SDE Frontend'),
        ('Data Analyst','Data Analyst'),
        ('Data Scientist','Data Scientist'),
        ('Machine Learning Engineer','Machine Learning Engineer'),
        ('Machine Learning Scientist','Machine Learning Scientist')
    )

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    last_login_time=models.DateTimeField(default=timezone.now)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    resume = models.ForeignKey(File,on_delete=models.SET_NULL,null=True,related_name='profile_file')
    academic_Record=models.TextField()
    internship_exp=models.TextField()
    research_exp=models.TextField()
    role=models.CharField(max_length=45,choices=roles) 

    def __str__(self):
        return self.user.username
