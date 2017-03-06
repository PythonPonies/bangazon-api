from rest_framework import viewsets
from bangazon_ultra.models import *
from bangazon_ultra.serializers import *
from rest_framework.permissions import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class PaymentViewSet(viewsets.ModelViewSet):
    ''' This class generates a list of all payment types stored in the database 
    Author: LaDonna Sales, Python Ponies
    '''
    # permission_classes = (IsAdminUser,)
    queryset = paymenttype_model.Payment_Type.objects.all()
    serializer_class = paymenttype_serializer.PaymentSerializer