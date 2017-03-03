from rest_framework import viewsets
from bangazonapi.models import *
from bangazonapi.serializers import *
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class OrderViewSet(viewsets.ModelViewSet):
    ''' The OrderViewSet class is a view that lists out all orders and details about a order.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Zoe LeBlanc, Python Ponies
    '''
    # permission_classes = (IsAdminUser,)
    queryset = order_model.Order.objects.all()
    serializer_class = order_serializer.OrderSerializer

class ProductOnOrderViewSet(viewsets.ModelViewSet):
    """
    The ProductOnOrderViewset class is a view that lists all associated products and orders.
   
    Additionally we also provide an extra `highlight` action.

    Author: Joey Kirby, Python Ponies
    """
    # permission_classes = (IsAdminUser,)
    queryset = order_model.Product_On_Order.objects.all()
    serializer_class = order_serializer.ProductOnOrderSerializer