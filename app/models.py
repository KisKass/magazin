from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)


class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField(upload_to="items")


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='cart_item', on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through=CartItem)


class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    email = models.EmailField()
