from rest_framework import serializers
from django.contrib.auth.models import User
from bangazonapi.models import User

#UserSerializer converts model data in JSON
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
