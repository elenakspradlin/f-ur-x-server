from django.db import models
from django.contrib.auth.models import User
from .registry_item_model import RegistryItem


class UserItems(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.OneToOneField(RegistryItem, on_delete=models.CASCADE)
