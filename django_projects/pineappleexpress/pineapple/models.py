from datetime import date
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User  # Required to assign User as a agent

import uuid  # Required for unique book instances


class Product(models.Model):
    """Model representing a product to include images as static"""
    name = models.CharField(max_length=150, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(blank=True)
    datelastorder = models.DateTimeField(blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
