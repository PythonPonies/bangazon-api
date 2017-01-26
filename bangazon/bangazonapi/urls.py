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
payment_detail = PaymentViewSet.as_view({
    'get': 'retrieve'
})
product_list = ProductViewSet.as_view({
    'get': 'list'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve'
})
product_category_list = ProductCategoryViewSet.as_view({
    'get': 'list'
})
product_category_detail = ProductCategoryViewSet.as_view({
    'get': 'retrieve'
})
product_on_order_list = ProductOnOrderViewSet.as_view({
    'get': 'list'
})
product_on_order_detail = ProductOnOrderViewSet.as_view({
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
    url(r'^product_categories/', product_category_list, name='product_category-list'),
    url(r'^product_categories/(?P<pk>[0-9]+)/', product_category_detail, name='product_category-detail'),
    url(r'^product_order/', product_on_order_list, name='product_on_order-list'),
    url(r'^product_order/(?P<pk>[0-9]+)/', product_on_order_detail, name='product_on_order-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)