# Generated by Django 4.0.5 on 2022-07-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0004_rename_mobileimage_mobile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='mobiledeliver',
            field=models.CharField(default='after 7 days', max_length=25),
        ),
        migrations.AddField(
            model_name='mobile',
            name='mobileoffer',
            field=models.CharField(default='20%', max_length=50),
        ),
    ]
