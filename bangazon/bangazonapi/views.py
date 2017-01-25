from bangazonapi.models import *
from bangazonapi.serializers import *
from rest_framework import generics
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    ''' The ProductsViewSet class is a view that lists out all products and details about a product.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Nathan Baker, Python Ponies
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    ''' This class generates a list of all payment types stored in the database '''
    queryset = Payment_Type.objects.all()
    serializer_class = PaymentSerializer

class UserViewSet(viewsets.ModelViewSet):
    ''' User viewset makes sense of the request and produces the appropriate output '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    ''' The OrderViewSet class is a view that lists out all orders and details about a order.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Zoe LeBlanc, Python Ponies
    '''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    ''' The CategoryViewSet class is a view that lists out all categories and details about a category.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Zoe LeBlanc, Python Ponies
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

