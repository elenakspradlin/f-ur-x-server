# stretch goal
from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    to_do_action = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
