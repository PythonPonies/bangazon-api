from django.shortcuts import render

# Create your views here.

class Products(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class Products_List(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer