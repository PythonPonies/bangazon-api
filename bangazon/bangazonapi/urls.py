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


#API endpoint that allows users to be viewed or edited.
urlpatterns = [
    url(r'^user/', user_list, name="user-list"),
    url(r'^user/(?P<pk>[0-9]+)/', user_detail, name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)


























    # url(r'^/users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list'),
    # url(r'^/users/', RetrieveAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-detail'),