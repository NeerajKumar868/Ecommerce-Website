# Generated by Django 4.0.5 on 2022-07-30 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_profile_city_remove_profile_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
    ]
