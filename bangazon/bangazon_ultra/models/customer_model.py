from django.db import models
from django.contrib.auth.models import User

# Model that instantiates a customer, and pulls in Django's default user model

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    phone = models.CharField(max_length=12, blank=True)
    shipping_address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)