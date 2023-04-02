from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    choice = (('garage', 'garage'), ('driver', 'driver'))
    type = models.CharField(max_length=20, choices=choice)
    phone = models.CharField(max_length=10)
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'



