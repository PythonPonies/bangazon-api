from django.db import models

# Create your models here.


class Payment_Type(models.Model):
	# class that represents the payment type table in database
	# all fields are currently visible in API
	# user = models.ForeignKey('User')
	account_number = models.CharField(max_length=100, blank=False)
	expiration_date = models.DateField()
	billing_address = models.TextField()
	payment_type = models.CharField(max_length=20)