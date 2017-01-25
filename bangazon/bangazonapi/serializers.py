from rest_framework import serializers
from bangazonapi.models import *


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'