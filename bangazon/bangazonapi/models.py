from django.db import models


# Create your models here.




#[ User Model contains the essential fields and behaviors of User Data. ]
class User(models.Model):
    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, blank=False, default='')
    shipping_address = models.TextField(max_length=100, blank=False, default='')
    email = models.EmailField(max_length=50, blank=False, default='')
    phone = models.CharField(max_length=50, blank=False, default='')
    date_joined = models.DateField(auto_now_add=True)

class Payment_Type(models.Model):
	'''class that represents the payment type table in database'''
	'''all fields are currently visible in API'''
	user = models.ForeignKey(User, null=True)
	account_number = models.CharField(max_length=100, blank=False)
	expiration_date = models.DateField()
	billing_address = models.TextField()
	payment_type = models.CharField(max_length=20)
    
class Order(models.Model):
    '''This class creates an Order table, with the fields of date_created, buyer_id, payment_type_id, and payment_complte'''
    date_created = models.DateField(auto_now_add=True)
    buyer = models.ForeignKey(User, null=True)
    payment_type = models.ForeignKey(Payment_Type, null=True)
    payment_complete = models.BooleanField(default=False)

