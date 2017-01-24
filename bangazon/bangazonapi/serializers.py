from rest_framework import serializers
from bangazonapi.models import *

class ProductsSerializer(serializers.ModelSerializer):
    Products = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = Products
        fields = ('id', 'title', 'description', 'price', 'quantity')

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        return instance