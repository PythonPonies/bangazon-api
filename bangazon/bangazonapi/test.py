from models import Payment_Type
from serializers import PaymentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

payment = Payment_Type(expiration_date = '01/01/2019')
payment.save()


if __name__ == '__main__':
	serializer = PaymentSerializer(payment)
	serializer.data
