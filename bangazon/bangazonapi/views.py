from bangazonapi.models import *
from bangazonapi.serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class ProductViewSet(viewsets.ModelViewSet):
    ''' The ProductsViewSet class is a view that lists out all products and details about a product.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Nathan Baker, Python Ponies
    '''
    permission_classes = (IsAdminUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class PaymentViewSet(viewsets.ModelViewSet):
    ''' This class generates a list of all payment types stored in the database 
    Author: LaDonna Sales, Python Ponies
    '''
    permission_classes = (IsAdminUser,)
    queryset = Payment_Type.objects.all()
    serializer_class = PaymentSerializer
    


class UserViewSet(viewsets.ModelViewSet):
    ''' 
    UserViewSet class is a view that lists out all Users and their details.

    Author: Joey Kirby, Python Ponies
    '''
    queryset = User.objects.all()
    def get_serializer_class(self):
        '''get_serializer_class checks if user is admin or not and changes the serialization fields depending on permissions'''
        if self.request.user.is_superuser:
            serializer_class = UserSerializer
        else:
            serializer_class = BasicUserSerializer
        return serializer_class

class OrderViewSet(viewsets.ModelViewSet):
    ''' The OrderViewSet class is a view that lists out all orders and details about a order.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Zoe LeBlanc, Python Ponies
    '''
    permission_classes = (IsAdminUser,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    ''' The CategoryViewSet class is a view that lists out all categories and details about a category.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Zoe LeBlanc, Python Ponies
    '''
    permission_classes = (IsAdminUser,)
    queryset = Product_Category.objects.all()
    serializer_class = ProductCategorySerializer
    

class ProductOnOrderViewSet(viewsets.ModelViewSet):
    """
    The ProductOnOrderViewset class is a view that lists all associated products and orders.
   
    Additionally we also provide an extra `highlight` action.

    Author: Joey Kirby, Python Ponies
    """
    permission_classes = (IsAdminUser,)
    queryset = Product_On_Order.objects.all()
    serializer_class = ProductOnOrderSerializer




