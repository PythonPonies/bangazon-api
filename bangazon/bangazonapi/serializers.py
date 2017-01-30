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
    seller = serializers.HyperlinkedIdentityField(view_name = "user-detail")

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
        model = User
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
        model = User
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
    # url = MultiplePKsHyperlinkedIdentityField(
    #     view_name='product-detail',
    #     lookup_fields=['product_id', 'pk'],
    #     lookup_url_kwargs=['product_pk', 'pk']
    # )
    # items = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='product_on_order-detail'
    # )
    class Meta:
        # model = Order
        # fields = ('url','date_created', 'buyer', 'payment_type', 'payment_complete', 'items')
        model = Product_On_Order
        fields = '__all__'
        depth = 1

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
    # products = ProductOnOrderSerializer(many=True)
    # order_items = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='product_on_order-list'
    # )
    class Meta:
        model = Order
        fields = '__all__'
        depth = 2

