from django.db import models
from django.contrib .auth.models import User
# Create your models here.


class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30, blank = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, blank=True)
    contact_picture = models.URLField(null=True, blank=True)
    is_favorite = models.BooleanField(default=False)
    