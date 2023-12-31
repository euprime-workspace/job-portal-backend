# Generated by Django 4.2.5 on 2023-10-11 20:24

import APIs.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('APIs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', APIs.models.CustomUserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='recruiter',
            old_name='phone',
            new_name='phone_number',
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_users', to='auth.group'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_users', to='auth.permission'),
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('webiste', models.CharField(max_length=50)),
                ('company_details', models.CharField(max_length=50, null=True)),
                ('company_docs', models.FileField(null=True, upload_to='company_files/')),
                ('designation', models.CharField(max_length=50)),
                ('compensation_CTC', models.IntegerField(default=None, null=True)),
                ('compensation_take_home', models.IntegerField(default=None, null=True)),
                ('compensation_bonus', models.IntegerField(blank=True, default=None, null=True)),
                ('bond_details', models.TextField(max_length=50, null=True)),
                ('selection_procedure_details', models.TextField(null=True)),
                ('tentative_date_of_joining', models.DateField(null=True)),
                ('tentative_no_of_offers', models.IntegerField(default=None, null=True)),
                ('offer_accepted', models.IntegerField(default=None, null=True)),
                ('deadline_datetime', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_offer', to='APIs.recruiter')),
            ],
        ),
    ]
