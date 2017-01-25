from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bangazonapi.views import *

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

#API endpoint that allows users to be viewed or edited.
urlpatterns = [
    url(r'^user/', user_list, name="user-list"),
    url(r'^user/(?P<pk>[0-9]+)/', user_detail, name="user-detail"),
      url(r'^orders/', order_list, name='order-list'),
    url(r'^orders/(?P<pk>[0-9]+)/', order_detail, name='order-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


























    # url(r'^/users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list'),
    # url(r'^/users/', RetrieveAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-detail'),
>>>>>>> e1125f6916d823c6abe14f0c71fa162d3e0ce442
