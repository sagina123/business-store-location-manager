from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('clothing', 'Clothing'),
        ('electronics', 'Electronics'),
        ('entertainment', 'Entertainment'),
        ('beauty', 'Beauty & Health'),
        ('accessories','Accessories'),
        ('jewellery','Jewellery'),
        ('pharmacy','Pharmacy'),
        ('foot wear','Footwear'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other', blank=True, null=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
