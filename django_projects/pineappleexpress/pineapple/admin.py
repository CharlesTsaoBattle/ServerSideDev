"""
admin.py
Created by Charles Tsao and Trent Williams
Last Updated: 01/03/2019
"""
from django.contrib import admin

# Models registered here.
from pineapple.models import Product

admin.site.register(Product)
