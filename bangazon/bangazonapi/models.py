from django.db import models

class User(models.Model):
    '''
    User Model contains the essential fields and behaviors of User Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Joey Kirby, Python Ponies
    '''
    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, blank=False, default='')
    shipping_address = models.TextField(max_length=100, blank=False, default='')
    email = models.EmailField(max_length=50, blank=False, default='')
    phone = models.CharField(max_length=50, blank=False, default='')
    date_joined = models.DateField(auto_now_add=True)

class Product_Category(models.Model):
    ''' The Category class is a model that defines which data is available in the Category table so a database can be created from it.

    Method List:
        -none

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc, Python Ponies
    '''
    category_name = models.CharField(max_length=50, blank=False, default='')

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
    categoryId = models.ForeignKey(Product_Category, null=True, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Payment_Type(models.Model):
	''' This class that represents the payment type table in database
	all fields are currently visible in API

    Author: LaDonna Sales, Python Ponies
    '''
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	account_number = models.CharField(max_length=100, blank=False)
	expiration_date = models.DateField()
	billing_address = models.TextField()
	payment_type = models.CharField(max_length=20)


class Order(models.Model):
    ''' The Order class is a model that defines which data is available in the Order table so a database can be created from it.

    Method List:
        -none

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc, Python Ponies
    Contributors: Steven Holmes, Python Ponies
    '''
    products = models.ManyToManyField('Product', through='Product_On_Order', 
                                     through_fields=('order', 'product'))
    date_created = models.DateField(auto_now_add=True)
    buyer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(Payment_Type, null=True, on_delete=models.CASCADE)
    payment_complete = models.BooleanField(default=False)


class Product_On_Order(models.Model):
    ''' 
    The Product On Order class is a model that defines a join table for Product & Order.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Joey Kirby, Python Ponies
    '''
    product = models.ForeignKey(Product, null=True)
    order = models.ForeignKey(Order, null=True)




