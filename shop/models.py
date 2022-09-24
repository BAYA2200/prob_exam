from django.db import models

# Create your models here.
from account.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=50)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
