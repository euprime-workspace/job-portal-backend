# Generated by Django 4.2.5 on 2023-10-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0005_merge_20231004_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Recruiter', 'Recruiter'), ('Candidate', 'Candidate')], max_length=9),
        ),
    ]