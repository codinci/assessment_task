from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    uid = models.CharField(max_length=36, unique=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    product_name = models.CharField(max_length=200)
    order_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product_name} ordered by {self.user.username} at {self.order_time}"
