from django.db import models
from clothes.models import *
from django.conf import settings
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    mens_shirts = models.ManyToManyField(Men_Shirt)
    mens_jackets = models.ManyToManyField(Men_Jacket)
    mens_pants = models.ManyToManyField(Men_Pants)
    mens_joggers = models.ManyToManyField(Men_Joggers)
    glasses = models.ManyToManyField(Glasses)
    earrings = models.ManyToManyField(Earring)
    necklaces = models.ManyToManyField(Necklace)
    women_shirts = models.ManyToManyField(Women_Shirt)
    women_jackets = models.ManyToManyField(Women_Jacket)
    women_pants = models.ManyToManyField(Women_Pants)
    women_joggers = models.ManyToManyField(Women_Joggers)
 