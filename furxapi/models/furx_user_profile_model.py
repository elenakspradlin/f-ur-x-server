from django.db import models
from django.contrib.auth.models import User
from datetime import date


class FURXUserProfileInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    day_of_breakup = models.DateField(default=date.today)

    # stretch goal
    # profile_picture = models.CharField(max_length=1000)

# need to come back to this-- property decorator?
   # @property
   # def full_name(self):
    #   return f'{self.user.first_name} {self.user.last_name}'
