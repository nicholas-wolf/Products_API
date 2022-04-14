from django.db import models
from review.models import Review



# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory_quantity = models.IntegerField()
    product_image = models.CharField(max_length=255)


   