# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0009_products_seller'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
