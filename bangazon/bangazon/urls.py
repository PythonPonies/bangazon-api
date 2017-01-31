''' bangazon URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
'''
from django.conf.urls import url, include
from django.contrib import admin
from bangazonapi import views
from rest_framework.routers import DefaultRouter
from bangazonapi.admin import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'product_categories', views.ProductCategoryViewSet)
router.register(r'product_on_order', views.ProductOnOrderViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    # url(r'^', include(order_router.urls)), 
]