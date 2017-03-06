from rest_framework import serializers
from bangazon_ultra.models import *

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    ''' The OrderSerializer class translates the Order models into other formats, in this case JSON by default. that Order table so a database can be created from it.

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Zoe LeBlanc, Python Ponies
    '''
    class Meta:
        model = order_model.Order
        fields = '__all__'
        depth = 3