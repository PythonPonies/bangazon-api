from rest_framework import serializers
from bangazonapi.models import *

class ProductsSerializer(serializers.ModelSerializer):
    Products = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = Products
        fields = ('id', 'title', 'description', 'price', 'quantity')