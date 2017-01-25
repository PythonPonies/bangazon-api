from bangazonapi.models import Products
from bangazonapi.serializers import ProductsSerializer
from rest_framework import generics

# Create your views here.

class ProductsList(generics.ListAPIView):
    """ The ProductsList class is a view that lists out all products.

    Argument List:
        -generics.ListAPIView: This method specifies that a collect of data is returned from the API.

    Author: Nathan Baker, Python Ponies
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductsDetail(generics.RetrieveAPIView):
    """ The ProductsDetail class is a view that lists details about one product.

    Argument List:
        -generics.RetrieveAPIView: This method specifies that one entry from the database is returned from the API.

    Author: Nathan Baker, Python Ponies
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer