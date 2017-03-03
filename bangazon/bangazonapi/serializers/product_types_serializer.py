from rest_framework import serializers
from bangazonapi.models import *

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    ''' The CategorySerializer class translates the Category models into other formats, in this case JSON by default. that Category table so a database can be created from it.

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Zoe LeBlanc, Python Ponies
    '''
    class Meta:
        model = product_types_model.Product_Type
        fields = '__all__'