from datetime import datetime
from django.db import models
from account.models import *
from cartapp.models import *
from django.utils import timezone

# Create your models here.



class Address(models.Model):
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    pincode=models.CharField(max_length=8)


class Order(models.Model):
    orderid=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    productlist=models.ManyToManyField(Product)
    orderdate=models.DateField(default=datetime.now())
    orderstatus=models.CharField(max_length=50,default="panding")
    billamount=models.FloatField()

def __str__(self):
    return f"{self.orderid},{self.orderdate},{self.orderstatus},{self.productlist.all}"