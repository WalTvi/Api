from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)

class CartItem(models.Model):
    user = models.ForeignKey(User, related_name='cart_items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()

class Sale(models.Model):
    user = models.ForeignKey(User, related_name='sales', on_delete=models.CASCADE)
    total_amount = models.FloatField()
    estimated_delivery_time = models.CharField(max_length=100)
