from django.db import models


class Feeling(models.Model):
    feeling = models.CharField(max_length=50)
