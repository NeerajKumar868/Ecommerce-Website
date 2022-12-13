# Generated by Django 4.0.5 on 2022-07-10 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0006_alter_mobile_mobiledeliver'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.mobile')),
            ],
        ),
    ]