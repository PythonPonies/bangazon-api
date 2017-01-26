# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 16:08
from __future__ import unicode_literals

from django.db import migrations

def load_orders(apps, schema_editor):
    '''load_orders loads initial seed data for Order table on makemigrations'''
        Order = apps.get_model("bangazonapi", "Order")
        order_1 = Order()
        order_1.save()
        order_2 = Order()
        order_2.save()
        order_3 = Order()
        order_3.save()

class Migration(migrations.Migration):
    '''Migration loads initial seed data for all tables on makemigrations'''

    dependencies = [
        ('bangazonapi', '0017_remove_order_product_on_order'),
    ]

    operations = [
        migrations.RunPython(load_orders),
    ]