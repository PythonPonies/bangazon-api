from rest_framework import serializers
from django.contrib.auth.models import User
from bangazon_ultra.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    ''' 
    UserSerializer converts model data in JSON 

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.
        
    Author: Joey Kirby, Python Ponies
    '''
    class Meta:
        model = User
        fields = ('id', 'last_name', 'username', 'email', 'first_name')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    ''' 
    BasicUserSerializer converts model data in JSON 

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.
        
    Author: Zoe LeBlanc, Python Ponies
    '''
    class Meta:
        model = customer_model.Customer
        fields = ('user', 'phone', 'shipping_address')
        depth = 1