from rest_framework import serializers
from bangazonapi.models import Payment_Type


class PaymentSerializer(serializers.ModelSerializer):
	# this class packages the payment type data fields into json format
	# all keys from the model are currently incorporated and will be visible on API calls
	class Meta :
		model = Payment_Type
		fields = ('user', 'account_number', 'expiration_date', 'billing_address', 'payment_type')


	# method to create and return a new instance of a payment type
	def create(self, validated_data):
		return Payment_Type.objects.create(**validated_data)

	# method to update existing payment type instance
	def update(self, instance, validated_data):
		instance.user = validated_data.get('user', instance.user)
		instance.account_number = validated_data.get('account_number', instance.account_number)
		instance.expiration_date = validated_data.get('expiration_date', instance.expiration_date)
		instance.billing_address = validated_data.get('billing_address', instance.billing_address)
		instance.payment_type = validated_data.get('payment_type', instance.payment_type)
		instance.save()
		return instance

