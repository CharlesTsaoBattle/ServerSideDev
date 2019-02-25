from datetime import date
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User  # Required to assign User as a agent

import uuid  # Required for unique book instances
