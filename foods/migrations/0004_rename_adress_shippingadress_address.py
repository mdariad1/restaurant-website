# Generated by Django 3.2.9 on 2022-01-10 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_rename_digital_product_deliverable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingadress',
            old_name='adress',
            new_name='address',
        ),
    ]
