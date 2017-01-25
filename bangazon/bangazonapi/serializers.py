from rest_framework import serializers
from bangazonapi.models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    ''' The ProductsSerializer class translates the Products models into other formats, in this case JSON by default. that Products table so a database can be created from it.

    Method List:
        -Meta
        -create
        -update

    Argument List:
        -serializers.ModelSerializer: This argument allows the class to access field types.

    Author: Nathan Baker, Python Ponies
    '''

    class Meta:
        ''' This method is tied to the ProductsSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        ''' This method creates a new entry in the Products table

        Argument List:
            -validated_data: This argument how you pass in the data for the new table entry
        '''
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        ''' This method creates a new entry in the Products table

        Argument List:
            -instance: This arguement is needed to update rather than replace data
            -validated_data: This argument how you pass in the data for the new table entry
        '''
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        return instance


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
	''' This class packages the payment type data fields into json format. All keys from the model are currently incorporated and will be visible on API calls '''

	class Meta :
		model = Payment_Type
		fields = '__all__'

	# def create(self, validated_data):
 #        ''' method to create and return a new instance of a payment type '''
	# 	return Payment_Type.objects.create(**validated_data)

	# def update(self, instance, validated_data):
 #        ''' method to update existing payment type instance '''
	# 	instance.user = validated_data.get('user', instance.user)
	# 	instance.account_number = validated_data.get('account_number', instance.account_number)
	# 	instance.expiration_date = validated_data.get('expiration_date', instance.expiration_date)
	# 	instance.billing_address = validated_data.get('billing_address', instance.billing_address)
	# 	instance.payment_type = validated_data.get('payment_type', instance.payment_type)
	# 	instance.save()
	# 	return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    ''' UserSerializer converts model data in JSON '''
    class Meta:
        model = User
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    ''' Creates Order Serializer and converts model into JSON '''
    class Meta:
        model = Order
        fields = '__all__'
<<<<<<< Updated upstream
=======

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    '''Creates Category Serializer and converts model into JSON'''
    class Meta:
        model = Category
        fields = '__all__'
>>>>>>> Stashed changes
