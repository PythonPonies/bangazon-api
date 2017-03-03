from rest_framework import viewsets
from bangazonapi.models import *
from bangazonapi.serializers import *
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class ProductTypeViewSet(viewsets.ModelViewSet):
    ''' The CategoryViewSet class is a view that lists out all categories and details about a category.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Zoe LeBlanc, Python Ponies
    '''
    # permission_classes = (IsAdminUser,)
    queryset = product_types_model.ProductType.objects.all()
    serializer_class = ProductCategorySerializer