# Generated by Django 4.2.5 on 2023-10-11 13:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0006_alter_customuser_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruiter',
            old_name='phone',
            new_name='phone_number',
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
                ('tier', models.CharField(choices=[['psu', 'PSU'], ['1', 'Tier 1'], ['2', 'Tier 2'], ['3', 'Tier 3'], ['4', 'Tier 4'], ['5', 'Tier 5'], ['6', 'Tier 6'], ['7', 'Tier 7'], ['8', 'Open Tier']], default=None, max_length=10, null=True)),
                ('tentative_date_of_joining', models.DateField(default=django.utils.timezone.now)),
                ('tentative_no_of_offers', models.IntegerField(default=None, null=True)),
                ('offer_accepted', models.IntegerField(default=None, null=True)),
                ('deadline_datetime', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_offer', to='APIs.recruiter')),
            ],
        ),
    ]
