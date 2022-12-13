
from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.
admin,status = Group.objects.get_or_create(name='admin')
customer,status = Group.objects.get_or_create(name='customer')


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_no=models.CharField(max_length=10)
    # address=models.CharField(max_length=255)
    # city=models.CharField(max_length=150,default='Mumbai')
    # state=models.CharField(max_length=150,default='Maharashtra')
    # country=models.CharField(max_length=150,default='India')
    # pincode=models.CharField(max_length=150,default=400072)
    def __str__(self):
        return self.user.username




    