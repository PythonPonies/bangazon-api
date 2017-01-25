from django.db import models

class Products(models.Model):
    """ The Products class is a model that defines which data is available in the Products table so a database can be created from it.

    Method List:
        -none

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Nathan Baker, Python Ponies
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    quantity = models.IntegerField()
    # categoryId = models.ForeignKey('Category')
    # seller_id = models.ForeignKey('Users')