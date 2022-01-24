"""This module contain the models to build the DB tables"""

from django.db import models
from django.contrib.auth.models import User
from app.config import config as c


class Category(models.Model):
    """Table containing products categories in DB"""

    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Table containing products in DB"""

    product_name_fr = models.CharField(max_length=200)
    brands = models.CharField(max_length=200)
    nutriscore_grade = models.CharField(max_length=1)
    stores = models.CharField(max_length=1000)
    url = models.CharField(max_length=2000)
    image = models.TextField(default=None)
    categories = models.ManyToManyField(Category)
    favorites = models.ManyToManyField(User, related_name="favorites")

    def __str__(self):
        return self.product_name_fr


class Rating(models.Model):
    """Table containing rates of users for products"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rate = models.PositiveSmallIntegerField(choices=c.RATE_CHOICES)

    def __str__(self):
        return self.user.username
