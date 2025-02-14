# Generated by Django 4.2.2 on 2023-07-18 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matrimony_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_Number', models.CharField(max_length=25)),
                ('Age', models.CharField(max_length=25)),
                ('Height', models.CharField(max_length=25)),
                ('Weight', models.CharField(max_length=25)),
                ('Blood_Group', models.CharField(max_length=25)),
                ('Marital_Status', models.CharField(max_length=25)),
                ('Nationality', models.CharField(max_length=25)),
                ('Mother_Tongue', models.CharField(max_length=25)),
                ('Workout', models.CharField(max_length=25)),
                ('Smoke', models.CharField(max_length=25)),
                ('Time_of_Birth', models.CharField(max_length=25)),
                ('Date_of_Birth', models.CharField(max_length=25)),
                ('Place_of_Birth', models.CharField(max_length=25)),
                ('Religion', models.CharField(max_length=25)),
                ('Cast', models.CharField(max_length=25)),
                ('Sub_Cast', models.CharField(max_length=25)),
                ('Education_Details', models.TextField()),
                ('Occupation_Details', models.TextField()),
                ('Side_Income', models.CharField(max_length=25)),
                ('Annual_Income', models.CharField(max_length=25)),
                ('Father_Name', models.CharField(max_length=25)),
                ('Father_Occupation', models.CharField(max_length=25)),
                ('Mother_Name', models.CharField(max_length=25)),
                ('Mother_Occupation', models.CharField(max_length=25)),
                ('No_of_Brothers', models.CharField(max_length=25)),
                ('No_of_Sisters', models.CharField(max_length=25)),
                ('Complexion', models.CharField(max_length=25)),
                ('Partner_Height', models.CharField(max_length=25)),
                ('Partner_Educationt', models.CharField(max_length=25)),
                ('Partner_Religion', models.CharField(max_length=25)),
                ('Partner_Preference', models.TextField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
