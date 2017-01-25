from bangazonapi.models import *
from bangazonapi.serializers import *
from rest_framework import generics
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    ''' The ProductsViewSet class is a view that lists out all products and details about a product.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specific data from the API.

    Author: Nathan Baker, Python Ponies
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    ''' Purpose: This class generates a list of all payment types stored in the database.
        Author: L.Sales, Python Ponies
        Arguments: viewsets.ModelViewSet 
    '''
    queryset = Payment_Type.objects.all()
    serializer_class = PaymentSerializer

class UserViewSet(viewsets.ModelViewSet):
    ''' User viewset makes sense of the request and produces the appropriate output '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    '''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

