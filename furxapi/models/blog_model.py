# stretch goal
from django.db import models
from django.contrib.auth.models import User
from .feeling_model import Feeling


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blog_post = models.CharField(max_length=5000)
    better_than_yesterday = models.BooleanField(default=False)
    feeling = models.ForeignKey(
        "Feeling", on_delete=models.CASCADE)
