from rest_framework import viewsets
from bangazonapi.models import *
from bangazonapi.serializers import *
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class PaymentViewSet(viewsets.ModelViewSet):
    ''' This class generates a list of all payment types stored in the database 
    Author: LaDonna Sales, Python Ponies
    '''
    # permission_classes = (IsAdminUser,)
    queryset = paymenttype_model.Payment_Type.objects.all()
    serializer_class = PaymentSerializer