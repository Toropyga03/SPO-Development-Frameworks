from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    delivery_address = models.TextField()
    promo_code = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
