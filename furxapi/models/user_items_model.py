from django.db import models
from django.contrib.auth.models import User
from .item_model import Item
from .user_profile_model import UserProfileInformation


class UserItem(models.Model):
    profile = models.ForeignKey(
        UserProfileInformation, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
