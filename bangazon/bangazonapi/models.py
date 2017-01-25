from django.db import models

class User(models.Model):
    '''User Model contains the essential fields and behaviors of User Data.'''
    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, blank=False, default='')
    shipping_address = models.TextField(max_length=100, blank=False, default='')
    email = models.EmailField(max_length=50, blank=False, default='')
    phone = models.CharField(max_length=50, blank=False, default='')
    date_joined = models.DateField(auto_now_add=True)

class Product(models.Model):
    ''' The Products class is a model that defines which data is available in the Products table so a database can be created from it.

    Method List:
        -none

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Nathan Baker, Python Ponies
    '''

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    quantity = models.IntegerField()
    # categoryId = models.ForeignKey('Category')
    seller = models.ForeignKey(User, null=True)

class Payment_Type(models.Model):
	''' This class that represents the payment type table in database
	all fields are currently visible in API
    '''
	user = models.ForeignKey(User, null=True)
	account_number = models.CharField(max_length=100, blank=False)
	expiration_date = models.DateField()
	billing_address = models.TextField()
	payment_type = models.CharField(max_length=20)

class Order(models.Model):
    ''' This class creates an Order table, with the fields of date_created, buyer_id, payment_type_id, and payment_complte
    '''
    date_created = models.DateField(auto_now_add=True)
    buyer = models.ForeignKey(User, null=True)
    payment_type = models.ForeignKey(Payment_Type, null=True)
    payment_complete = models.BooleanField(default=False)
    product_on_order = models.ManyToManyField(Product, null=True)

class Category(models.Model):
    '''This class creates an Order table, with the fields of date_created, buyer_id, payment_type_id, and payment_complete'''
    category_name = models.CharField(max_length=50, blank=False, default='')

