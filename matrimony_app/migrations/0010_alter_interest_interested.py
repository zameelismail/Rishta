# Generated by Django 4.2.2 on 2023-07-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_app', '0009_interest_user_profile_alter_interest_interested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='interested',
            field=models.IntegerField(default=0),
        ),
    ]
