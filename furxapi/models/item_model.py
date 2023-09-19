from django.db import models


class Item(models.Model):
    name = picture = models.CharField(max_length=1000)
    picture = models.CharField(max_length=1000)
    price = models.CharField(max_length=10)
    url = models.CharField(max_length=2000)
