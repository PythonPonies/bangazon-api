from django.db import models

# Create your models here.
class Order(models.Model):
    '''This class creates an Order table, with the fields of date_created, buyer_id, payment_type_id, and payment_complte'''
    date_created = models.DateField(auto_now_add=True)
    # buyer = models.ForeignKey('User.id', on_delete=models.CASCADE)
    # payment_type = models.ForeignKey('Payment_Types.id', on_delete=models.CASCADE)
    payment_complete = models.BooleanField(default=False)
