# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 16:08
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import migrations, models



def load_orders(apps, schema_editor):
    '''load_orders loads initial seed data for Order table on makemigrations'''
    Order = apps.get_model("bangazon_ultra", "Order")
    order_1 = Order()
    order_1.save()
    order_2 = Order()
    order_2.save()
    order_3 = Order()
    order_3.save()

def load_product_categories(apps, schema_editor):
    '''load_product_categories loads initial seed data for Product Categories table on makemigrations'''
    Product_Type = apps.get_model("bangazon_ultra", "Product_Type")
    product_category_1 = Product_Type(category_name="shoes")
    product_category_1.save()
    product_category_2 = Product_Type(category_name="books")
    product_category_2.save()
    product_category_3 = Product_Type(category_name="movies")
    product_category_3.save()

# def load_customers(apps, schema_editor):
#     '''load_users loads initial seed data for User table on makemigrations'''
#     # User = apps.get_model("bangazon_ultra", "User")
#     user_1 = User.objects.create_user(first_name="Zoe", last_name="LeBlanc", email="z@z.com", username="Zoe")
#     user_2 = User.objects.create_user(first_name="Steve", last_name="Brownlee", email="s@b.com", username="Steve")
#     user_3 = User.objects.create_user(first_name="Joey", last_name="Kirby", email="j@k.com", username="Joey")
#     Customer = apps.get_model("bangazon_ultra", "Customer")
#     customer_1 = Customer(user=user_1, shipping_address="500 Interstate Blvd, Nashville, TN", phone="4132143827")
#     customer_1.save()
#     customer_2 = Customer(user=user_2, shipping_address="500 Interstate Blvd, Nashville, TN", phone="4232243827")
#     customer_2.save()
#     customer_3 = Customer(user=user_3, shipping_address="500 Interstate Blvd, Nashville, TN", phone="4333343837")
#     customer_3.save()


def load_products(apps, schema_editor):
    '''load_products loads initial seed data for Products table on makemigrations'''
    Product = apps.get_model("bangazon_ultra", "Product")
    product_1 = Product(title="Computer", description="New macbook", price=900.00, quantity=4)
    product_1.save()
    product_2 = Product(title="coffee mug", description="new mugs", price=9.00, quantity=4)
    product_2.save()
    product_3 = Product(title="Car", description="New car", price=9000.00, quantity=4)
    product_3.save()

def load_payment_types(apps, schema_editor):
    '''load_payment_types loads initial seed data for Payment Types table on makemigrations'''
    Payment_Type = apps.get_model("bangazon_ultra", "Payment_Type")
    payment_type_1 = Payment_Type(account_number="54545454", billing_address="X", expiration_date="2017-01-27", payment_name="mastercard")
    payment_type_1.save()
    payment_type_2 = Payment_Type(account_number="54545454", billing_address="X", expiration_date="2017-01-27",payment_name="mastercard")
    payment_type_2.save()
    payment_type_3 = Payment_Type(account_number="54545454", billing_address="X", expiration_date="2017-01-27",payment_name="mastercard")
    payment_type_3.save()

def load_product_on_orders(apps, schema_editor):
    '''load_product_on_orders loads initial seed data for Product On Order table on makemigrations'''
    Product_On_Order = apps.get_model("bangazon_ultra", "Product_On_Order")
    product_on_order_1 = Product_On_Order()
    product_on_order_1.save()
    product_on_order_2 = Product_On_Order()
    product_on_order_2.save()
    product_on_order_3 = Product_On_Order()
    product_on_order_3.save()

class Migration(migrations.Migration):
    '''Migration loads initial seed data for all tables on makemigrations'''

    dependencies = [
        ('bangazon_ultra', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_orders),
        migrations.RunPython(load_product_categories),
        # migrations.RunPython(load_customers),
        migrations.RunPython(load_products),
        migrations.RunPython(load_product_on_orders),
        migrations.RunPython(load_payment_types),
    ]