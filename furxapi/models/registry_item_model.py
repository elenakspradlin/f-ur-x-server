from django.db import models
from django.contrib.auth.models import User


class RegistryItem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # should I add a name property?
    picture = models.CharField(max_length=1000)
    price = models.CharField(max_length=10)
    url = models.URLField(max_length=200)
