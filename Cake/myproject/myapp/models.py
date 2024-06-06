
from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=200)
    product_image = models.ImageField()
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    description = models.TextField()



