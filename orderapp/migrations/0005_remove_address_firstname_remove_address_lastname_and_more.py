# Generated by Django 4.0.5 on 2022-07-31 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0004_rename_first_name_address_firstname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='address',
            name='LastName',
        ),
        migrations.AlterField(
            model_name='order',
            name='orderdate',
            field=models.DateField(default=datetime.datetime(2022, 7, 31, 16, 55, 35, 599334)),
        ),
    ]
