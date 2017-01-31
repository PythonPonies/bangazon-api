from rest_framework import serializers
from bangazonapi.models import *

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    ''' The ProductsSerializer class translates the Products models into other formats, in this case JSON by default. that Products table so a database can be created from it.

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Nathan Baker, Python Ponies
    '''
    class Meta:
        ''' This method is tied to the ProductsSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = Product
        fields = '__all__'


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    ''' This class packages the payment type data fields into json format. All keys from the model are currently incorporated and will be visible on API calls 
    
    Author: LaDonna Sales, Python Ponies
    '''
    class Meta :
        ''' This method is tied to the ProductsSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = Payment_Type
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    ''' 
    UserSerializer converts model data in JSON 

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.
        
    Author: Joey Kirby, Python Ponies
    '''
    class Meta:
        model = Customer
        fields = '__all__'

class BasicUserSerializer(serializers.HyperlinkedModelSerializer):
    ''' 
    BasicUserSerializer converts model data in JSON 

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.
        
    Author: Zoe LeBlanc, Python Ponies
    '''
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'id')



class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    ''' The CategorySerializer class translates the Category models into other formats, in this case JSON by default. that Category table so a database can be created from it.

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Zoe LeBlanc, Python Ponies
    '''
    class Meta:
        model = Product_Category
        fields = '__all__'


class ProductOnOrderSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Creates ProductOrder Serializer and converts model into JSON

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.
        
    Author: Joey Kirby, Python Ponies
    '''
    class Meta:
        model = Product_On_Order
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    ''' The OrderSerializer class translates the Order models into other formats, in this case JSON by default. that Order table so a database can be created from it.

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Zoe LeBlanc, Python Ponies
    '''
    class Meta:
        model = Order
        fields = '__all__'
        depth = 3

