from django.db.models import DateField
from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=255)
    product_category = models.CharField(max_length=50, default="")
    sub_product_category = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=255, blank=True)
    published_date = models.DateField()
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to="products/images", default="")
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
