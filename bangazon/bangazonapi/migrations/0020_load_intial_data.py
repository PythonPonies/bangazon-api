# Good example for a data migration
from django.db import migrations
from django.core.serializers import base, python
from django.core.management import call_command



class Migration(migrations.Migration):
    dependencies = [
        ('bangazonapi', '0014_product_on_order'),
    ]

    operations = [
    ]