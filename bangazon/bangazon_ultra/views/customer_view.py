from rest_framework import viewsets
from bangazon_ultra.models import *
from bangazon_ultra.serializers import *
from rest_framework.permissions import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    ''' 
    UserViewSet class is a view that lists out all Users and their details.

    Author: Joey Kirby, Python Ponies
    '''
    queryset = User.objects.all()
    def get_serializer_class(self):
        '''get_serializer_class checks if user is admin or not and changes the serialization fields depending on permissions'''
        if self.request.user.is_superuser:
            serializer_class = customer_serializer.UserSerializer
        else:
            serializer_class = customer_serializer.BasicUserSerializer
        return serializer_class
    

class CustomerViewSet(viewsets.ModelViewSet):
    ''' The CustomerViewSet class is a view that lists out all Customers and details about a Customer.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Zoe LeBlanc, Python Ponies
    '''
    # permission_classes = (IsAdminUser,)
    queryset = customer_model.Customer.objects.all()
    serializer_class = customer_serializer.CustomerSerializer