# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0004_auto_20170130_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='bangazonapi.Product_On_Order', to='bangazonapi.Product'),
        ),
        migrations.AlterField(
            model_name='product_on_order',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Order'),
        ),
        migrations.AlterField(
            model_name='product_on_order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bangazonapi.Product'),
        ),
    ]