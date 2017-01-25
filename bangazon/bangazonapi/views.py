from bangazonapi.models import Products
from bangazonapi.serializers import ProductsSerializer
from rest_framework import generics

# Create your views here.

class ProductsList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductsDetail(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


    # queryset = Products.objects.all() # this doesn't work
    # serializer_class = ProductsSerializer

    # # AssertionError: 'ProductsList' should either include a `queryset` attribute, or override the `get_queryset()` method.




# # Create your views here.
# #generates a list of all payment types stored in the database
# class PaymentTypeList(generics.ListAPIView):
#     queryset = Payment_Type.objects.all()
#     serializer_class = PaymentSerializer

# #generates the specific detail for a payment type
# class PaymentTypeDetail(generics.RetrieveAPIView):
#     queryset = Payment_Type.objects.all()
#     serializer_class = PaymentSerializer