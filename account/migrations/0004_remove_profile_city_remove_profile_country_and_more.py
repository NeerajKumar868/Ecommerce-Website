# Generated by Django 4.0.5 on 2022-07-23 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
    ]
