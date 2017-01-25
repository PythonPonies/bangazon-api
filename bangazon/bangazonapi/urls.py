from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bangazonapi.views import *

"""Defining urls and views"""
order_list = OrderViewSet.as_view({
    'get': 'list'
})
order_detail = OrderViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^orders/', order_list, name='order-list'),
    url(r'^orders/(?P<pk>[0-9]+)/', order_detail, name='order-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)