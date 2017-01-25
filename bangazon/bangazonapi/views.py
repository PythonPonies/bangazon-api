from bangazonapi.models import Payment_Type
from bangazonapi.serializers import PaymentSerializer
from rest_framework import generics

# Create your views here.
#generates a list of all payment types stored in the database
class PaymentTypeList(generics.ListAPIView):
    queryset = Payment_Type.objects.all()
    serializer_class = PaymentSerializer

#generates the specific detail for a payment type
class PaymentTypeDetail(generics.RetrieveAPIView):
    queryset = Payment_Type.objects.all()
    serializer_class = PaymentSerializer