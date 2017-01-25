from django.conf.urls import url
from bangazonapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^payment/$', views.PaymentTypeList.as_view()),
    url(r'^payment/(?P<pk>[0-9]+)/$', views.PaymentTypeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)