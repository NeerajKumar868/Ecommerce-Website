# Generated by Django 4.0.5 on 2022-07-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Mumbai', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='India', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.CharField(default=400072, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='Maharashtra', max_length=150),
        ),
    ]
