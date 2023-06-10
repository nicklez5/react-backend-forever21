from datetime import *
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, UserManager
# Create your models here.
class Men_Shirt(models.Model):
    img_url = models.URLField(max_length=500)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
#
class Men_Jacket(models.Model):
    img_url = models.URLField(max_length=500)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
class Men_Pants(models.Model):
    img_url = models.URLField(max_length=500)
    waist_size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
class Men_Joggers(models.Model):
    img_url = models.URLField(max_length=500)
    waist_size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
class Glasses(models.Model):
    img_url = models.URLField(max_length=500)
    price = models.FloatField()
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
class Earring(models.Model):
    img_url = models.URLField(max_length=500)
    price = models.FloatField()
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
class Necklace(models.Model):
    img_url = models.URLField(max_length=500)
    price = models.FloatField()
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
class Women_Shirt(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    img_url = models.URLField(max_length=500)
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
class Women_Jacket(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    img_url = models.URLField(max_length=500)
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
class Women_Pants(models.Model):
    img_url = models.URLField(max_length=500)
    waist_size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
class Women_Joggers(models.Model):
    img_url = models.URLField(max_length=500)
    waist_size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    @property
    def total_price(self):
        return self.quantity * self.price
    



# Create your models here.
