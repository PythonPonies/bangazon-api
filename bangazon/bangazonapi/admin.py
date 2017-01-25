from django.contrib import admin
from bangazonapi.models import *

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Payment_Type)
admin.site.register(Product)