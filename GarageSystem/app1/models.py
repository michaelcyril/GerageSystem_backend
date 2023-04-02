from django.db import models
from AuthUser.models import User


# Create your models here.

class Garage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'garage'

    def __str__(self):
        return f'{self.name}'


class Engineer(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    description = models.TextField()
    garage_id = models.ForeignKey(Garage, on_delete=models.CASCADE)

    class Meta:
        db_table = 'engineer'

    def __str__(self):
        return f'{self.username} at {self.garage_id.name}'


class FeedBack(models.Model):
    garage_id = models.ForeignKey(Garage, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.TextField()

    def __str__(self):
        return f'{self.garage_id.name} - {self.feed}'

    class Meta:
        db_table = 'feedback'

