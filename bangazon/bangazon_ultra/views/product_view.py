from rest_framework import viewsets
from bangazon_ultra.models import *
from bangazon_ultra.serializers import *
from rest_framework.permissions import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class ProductViewSet(viewsets.ModelViewSet):
    ''' The ProductsViewSet class is a view that lists out all products and details about a product.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Nathan Baker, Python Ponies
    '''
    # permission_classes = (IsAdminUser,)
    queryset = products_model.Product.objects.all()
    serializer_class = product_serializer.ProductSerializer