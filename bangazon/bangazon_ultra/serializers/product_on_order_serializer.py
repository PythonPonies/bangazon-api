from rest_framework import serializers
from bangazon_ultra.models import *

class ProductOnOrderSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Creates ProductOrder Serializer and converts model into JSON

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.
        
    Author: Joey Kirby, Python Ponies
    '''
    class Meta:
        model = order_model.Product_On_Order
        fields = '__all__'