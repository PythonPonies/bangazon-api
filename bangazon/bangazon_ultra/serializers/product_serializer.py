from rest_framework import serializers
from bangazon_ultra.models import *

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    ''' The ProductsSerializer class translates the Products models into other formats, in this case JSON by default. that Products table so a database can be created from it.

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Nathan Baker, Python Ponies
    '''
    class Meta:
        ''' This method is tied to the ProductsSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = products_model.Product
        fields = '__all__'