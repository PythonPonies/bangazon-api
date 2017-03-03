from rest_framework import viewsets
from bangazonapi.models import *
from bangazonapi.serializers import *
from rest_framework.permissions import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    ''' 
    UserViewSet class is a view that lists out all Users and their details.

    Author: Joey Kirby, Python Ponies
    '''
    queryset = User.objects.all()
    serializer_class = customer_serializer.UserSerializer
    

class CustomerViewSet(viewsets.ModelViewSet):
    ''' The CustomerViewSet class is a view that lists out all Customers and details about a Customer.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Zoe LeBlanc, Python Ponies
    '''
    # permission_classes = (IsAdminUser,)
    queryset = customer_model.Customer.objects.all()
    serializer_class = customer_serializer.CustomerSerializer