from django.contrib import admin
from django.contrib.auth.models import User
from bangazonapi.models import *

admin.site.register(customer_model.Customer)
admin.site.register(order_model.Order)
admin.site.register(paymenttype_model.Payment_Type)
admin.site.register(products_model.Product)
admin.site.register(product_types_model.Product_Type)
admin.site.register(order_model.Product_On_Order)
