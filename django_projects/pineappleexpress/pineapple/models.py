from datetime import date
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User  # Required to assign User as a agent

import uuid  # Required for unique book instances


class Product(models.Model):
    """Model representing a product"""
    name = models.CharField(max_length=150, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(blank=True)
    datelastorder = models.DateTimeField(blank=True)
#    image = models.ImageField(blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])



#    CAN ALL THE BELOW BE REMOVED?

# class ProductInstance(models.Model):
#     """Model representing a specific instance of a product"""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     product_name = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
#     customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         ordering = ['product_name']
        
#     def __str__(self):
#         """String for representing the Model object."""
#         return '{0} ({1})'.format(self.id, self.product.product_name)


# class Customer(models.Model):

#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     customer_username = models.CharField(max_length=30)
#     email_address = models.CharField(max_length=30)
#     phone_number = models.CharField(max_length=15)

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
