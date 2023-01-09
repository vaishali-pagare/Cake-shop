from django.db import models
from adminApp.models import Product,userInfo
from datetime import datetime

# Create your models here.
class MyCart(models.Model):
    user = models.ForeignKey(to='adminApp.userInfo',on_delete=models.CASCADE)
    cake = models.ForeignKey(to='adminApp.Product',on_delete=models.CASCADE)
    qty = models.IntegerField()
    class Meta:
        db_table = "MyCart"
        
class OrderMaster(models.Model):
    user = models.ForeignKey(to='adminApp.userInfo',on_delete=models.CASCADE)
    amount = models.FloatField(default=1000)
    date = models.DateTimeField(default=datetime.now)
    details = models.CharField(max_length=20)
    class Meta:
        db_table = "OrderMaster"


