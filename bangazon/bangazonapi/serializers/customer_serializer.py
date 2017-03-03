from rest_framework import serializers
from django.contrib.auth.models import User
from bangazonapi.models import *


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
        fields = '__all__'
        depth = 1

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
        fields = '__all__'