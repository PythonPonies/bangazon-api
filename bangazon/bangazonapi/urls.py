from django.conf.urls import url
from bangazonapi.views import *
from rest_framework.urlpatterns import format_suffix_patterns

#defines urls
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
order_list = OrderViewSet.as_view({
    'get': 'list'
})
order_detail = OrderViewSet.as_view({
    'get': 'retrieve'
})
payment_list = PaymentViewSet.as_view({
    'get': 'list'
})
payent_detail = PaymentViewSet.as_view({
    'get': 'retrieve'
})
product_list = ProductViewSet.as_view({
    'get': 'list'
})
product_detail = ProductViewSet.as_view({
category_list = CategoryViewSet.as_view({
    'get': 'list'
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve'
})

#API endpoint that allows users to be viewed or edited.
urlpatterns = [
    url(r'^users/', user_list, name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/', user_detail, name="user-detail"),
    url(r'^orders/', order_list, name='order-list'),
    url(r'^orders/(?P<pk>[0-9]+)/', order_detail, name='order-detail'),
    url(r'^payments/', payment_list, name='payment-list'),
    url(r'^payments/(?P<pk>[0-9]+)/', payment_detail, name='payment-detail'),
    url(r'^products/', product_list, name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/', product_detail, name='product-detail'),
    url(r'^categories/', category_list, name='category-list'),
    url(r'^categories/(?P<pk>[0-9]+)/', category_detail, name='category-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)