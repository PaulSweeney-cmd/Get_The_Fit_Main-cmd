# Generated by Django 3.2.7 on 2021-10-22 18:18

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store_checkout', '0009_auto_20211021_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]