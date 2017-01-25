from rest_framework import serializers
from bangazonapi.models import *

#UserSerializer converts model data in JSON
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    '''Creates Order Serializer and converts model into JSON'''
    class Meta:
        model = Order
        fields = '__all__'


