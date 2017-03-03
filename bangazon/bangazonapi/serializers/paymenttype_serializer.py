from rest_framework import serializers
from bangazonapi.models import *

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    ''' This class packages the payment type data fields into json format. All keys from the model are currently incorporated and will be visible on API calls 
    
    Author: LaDonna Sales, Python Ponies
    '''
    class Meta :
        ''' This method is tied to the ProductsSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = paymenttype_model.Payment_Type
        fields = '__all__'