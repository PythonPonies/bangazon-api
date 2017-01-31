# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0002_load_initial_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='bangazonapi.Product_On_Order', to='bangazonapi.Product'),
        ),
    ]