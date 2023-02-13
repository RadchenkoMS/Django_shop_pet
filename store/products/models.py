from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    amount = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    value = models.FloatField(blank=False, null=False)
    discount = models.FloatField(blank=False, null=False)


class Product_image(models.Model):
    photo = models.ImageField()



