import datetime
from tkinter import TRUE
from django.db import models

# Create your models here.



class CustomerDetailsModel(models.Model):
    cus_id = models.BigAutoField(primary_key=True)
    cus_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)

    def __str__(self): 
        return self.cus_name

class ProductModel(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self): 
        return self.product_name

class UnitModel(models.Model):
    unit_id = models.BigAutoField(primary_key=True)
    product_id = models.ForeignKey(ProductModel, related_name='units' ,on_delete=models.CASCADE)
    unit = models.CharField(max_length=20, default='Unit not set')

    def __str__(self): 
        return self.unit   

class OrderListModel(models.Model):    
    order_id = models.BigAutoField(primary_key=True)
    order_no = models.CharField(max_length=150, blank=True, null=True)
    cus_id= models.ForeignKey(CustomerDetailsModel, on_delete=models.CASCADE)
    order_date = models.CharField(max_length=50, null=True, blank=True, default=None)
    description = models.CharField(max_length=1000, null=True, blank=True, default=None)
    total_amount = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self): 
        return self.order_no

class OrderDetailsModel(models.Model):
    ordered_id = models.BigAutoField(primary_key=True)
    order_id = models.ForeignKey(OrderListModel, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    unit_ordered = models.CharField(max_length=20)
    price_ordered = models.DecimalField(max_digits=50, decimal_places=2)
    quantity_ordered = models.IntegerField()
    total_amount_ordered = models.DecimalField(max_digits=50, decimal_places=2)


