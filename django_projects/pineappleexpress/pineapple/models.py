"""
models.py
Created by Charles Tsao and Trent Williams
Last Updated: 01/03/2019
"""

from datetime import date
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User  # Required to assign User as a agent


# Product Model for all products in the Pineapple Express Store
class Product(models.Model):
    """Model representing a product"""
    name = models.CharField(max_length=75, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    description = models.TextField(max_length=500, blank=True) # Can leave description blank
    quantity = models.IntegerField(blank=False)
    datelastorder = models.DateTimeField(blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
