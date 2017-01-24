from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    quantity = models.IntegerField()
    # categoryId = models.ForeignKey('Category')
    # seller_id = models.ForeignKey('Users')