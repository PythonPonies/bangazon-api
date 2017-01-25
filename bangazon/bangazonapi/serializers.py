from rest_framework import serializers
from bangazonapi.models import *

class ProductsSerializer(serializers.ModelSerializer):
    """ The ProductsSerializer class translates the Products models into other formats, in this case JSON by default. that Products table so a database can be created from it.

    Method List:
        -Meta
        -create
        -update

    Argument List:
        -serializers.ModelSerializer: This argument allows the class to access field types.

    Author: Nathan Baker, Python Ponies
    """

    class Meta:
        """ This method is tied to the ProductsSerializer class and tells the serializer to serialize all fields in the table.
        """
        model = Products
        fields = '__all__'

    def create(self, validated_data):
        """ This method creates a new entry in the Products table

        Argument List:
            -validated_data: This argument how you pass in the data for the new table entry
        """
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ This method creates a new entry in the Products table

        Argument List:
            -instance: This arguement is needed to update rather than replace data
            -validated_data: This argument how you pass in the data for the new table entry
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        return instance