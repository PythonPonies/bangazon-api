from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    shipping_address = models.CharField()
    email = models.EmailField()