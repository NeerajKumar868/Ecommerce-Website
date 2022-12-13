from django.db import models

# Create your models here.
class Mobile(models.Model):
    mobileid=models.AutoField(primary_key=True)
    mobilename=models.TextField(max_length=50) 
    mobileprice=models.FloatField(max_length=20)
    mobilediscription=models.TextField(max_length=50)
    mobileoffer=models.CharField(max_length=50,default='20%')
    mobiledeliver=models.CharField(max_length=55,default='after 7 days')
    image=models.ImageField(upload_to='Image',default='No Image')