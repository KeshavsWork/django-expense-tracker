from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="expenses")
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    PAYMENT_CHOICES = [
        ("cash", "Cash"),
        ("card", "Card"),
        ("upi", "UPI"),
        ("other", "Other"),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default="cash")

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"
