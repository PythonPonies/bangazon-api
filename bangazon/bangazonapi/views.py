from bangazonapi.serializers import *
from bangazonapi.models import *
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
  
