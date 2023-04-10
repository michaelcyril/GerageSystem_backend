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


class FeedBackRequest(models.Model):
    choice = (('no', 'no'), ('yes', 'tes'), ('approved', 'approved'))
    garage_id = models.ForeignKey(Garage, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    is_received = models.CharField(default='no', choices=choice)

    def __str__(self):
        return f'{self.garage_id.name} - {self.driver_id.name}'

    class Meta:
        db_table = 'feedback_request'


class FeedBackAppointment(models.Model):
    choice = (('no', 'no'), ('yes', 'tes'), ('approved', 'approved'))
    garage_id = models.ForeignKey(Garage, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.CharField(max_length=200)
    is_received = models.CharField(default='no', choices=choice)

    def __str__(self):
        return f'{self.garage_id.name} - {self.driver_id.name}'

    class Meta:
        db_table = 'feedback_appontment'