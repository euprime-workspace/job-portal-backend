from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager,PermissionsMixin,Group, Permission
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid

from simple_history.models import HistoricalRecords

class CustomUserManager(UserManager):
    def _create_user(self,username,password,**extra_fields):
        if not username:
            raise ValueError("Invalid username field")
        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self,username=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(username,password,**extra_fields)
    
    def create_superuser(self,username=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(username,password,**extra_fields)
    
    def clean_fields(self, *args, **kwargs):
        super().clean_fields(*args, **kwargs)

        try:
            uuid.UUID(str(self.instance.ID))
        except ValueError:
            raise ValidationError({'ID': ['Invalid UUID string for ID field.']})

class File(models.Model):
    uploaded_file = models.FileField(upload_to="uploads/")
    history = HistoricalRecords()

    def __str__(self):
        return self.uploaded_file.name

class CustomUser(AbstractBaseUser,PermissionsMixin):
    userTypes=(
        ("Recruiter","Recruiter"),
        ("Candidate","Candidate")
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    user_type=models.CharField(max_length=9,choices=userTypes)

    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users')

    objects=CustomUserManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['password','user_type']

    def __str__(self):
        return self.username


class Recruiter(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    company = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="recruitor")

    def __str__(self):
        return self.user.username


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

class JobDescription(models.Model):
    company_name=models.CharField(max_length=50)
    address=models.TextField()
    webiste=models.CharField(max_length=300)
    company_details=models.CharField(max_length=50,null=True)
    company_docs=models.FileField(upload_to="company_files/",null=True)
    contact_person=models.ForeignKey(Recruiter,related_name="job_offer",on_delete=models.CASCADE)
    designation=models.CharField(max_length=50)
    compensation_CTC=models.IntegerField(null=True,default=None)
    compensation_take_home = models.IntegerField(blank=False, default=None, null=True)
    compensation_bonus = models.IntegerField(blank=True, default=None, null=True)
    bond_details=models.TextField(max_length=50,null=True)
    selection_procedure_details=models.TextField(null=True)
    tentative_date_of_joining = models.DateField(null=True)
    tentative_no_of_offers = models.IntegerField(default=None,null=True)
    offer_accepted=models.IntegerField(default=None,null=True)
    deadline_datetime = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name