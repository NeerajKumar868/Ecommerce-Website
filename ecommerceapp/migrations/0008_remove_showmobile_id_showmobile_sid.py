# Generated by Django 4.0.5 on 2022-07-10 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0007_showmobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showmobile',
            name='id',
        ),
        migrations.AddField(
            model_name='showmobile',
            name='sid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
