# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0010_auto_20170125_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product_on_order',
            field=models.ManyToManyField(null=True, to='bangazonapi.Product'),
        ),
    ]
