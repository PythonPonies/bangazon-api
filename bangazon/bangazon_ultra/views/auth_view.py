from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from bangazon_ultra.serializers import *
from bangazon_ultra.models import *

def logincustomer_view(request):
    permission_classes = (AllowAny,)

    req_body = json.loads(request.body.decode())
    username = req_body['username']
    password = req_body['password']
    user = authenticate(username=username, password=password)

    success = False
    if user is not None:
        if user.is_active:
            login(request, user)
            data = json.dumps({
                'success': True,
                'username': user.username,
                'email': user.email,
            })
            return HttpResponse(data, content_type='application/json')

        return HttpResponse(self._error_response('disabled'), content_type='application/json')
    return HttpResponse(self._error_response('invalid'), content_type='application/json')

class LoginView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = json.dumps({
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        })

    def post(self, request):
        return logincustomer_view(request)

class RegisterView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = json.dumps({
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        })

    # @csrf_exempt
    def post(self,request):
        permission_classes = (AllowAny,)

        req_body = json.loads(request.body.decode())
        print(req_body)
        user = User.objects.create_user(
            username = req_body['username'], 
            password = req_body['password'], 
            email = req_body['email'], 
            first_name = req_body['first_name'],
            last_name = req_body['last_name']
            )
        customer = customer_model.Customer.objects.create(
            user = user, 
            phone = req_body['phone'], 
            shipping_address=req_body['shipping_address']
            )
        return logincustomer_view(request)


