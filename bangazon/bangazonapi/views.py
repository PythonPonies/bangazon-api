from bangazonapi.models import *
from bangazonapi.serializers import *
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.
#generates a list of all payment types stored in the database
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment_Type.objects.all()
    serializer_class = PaymentSerializer

# Create your views here.
#user viewset makes sense of the request and produces the appropriate output
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



