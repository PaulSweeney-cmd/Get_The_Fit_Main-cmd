# Generated by Django 3.2.7 on 2021-10-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_checkout', '0002_alter_order_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item_total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, null=True),
        ),
    ]
