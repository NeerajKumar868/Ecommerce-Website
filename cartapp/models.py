from pyexpat import model
from django.db import models
from ecommerceapp.models import *
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.pid} {self.mobile} {self.quantity}'


class Cart(models.Model):
    cartid=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    productlist=models.ManyToManyField(Product)


    def __str__(self) -> str:
        return f'{self.cartid} {self.productlist.all()} '