# Generated by Django 4.2.2 on 2023-07-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_app', '0011_profile_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
