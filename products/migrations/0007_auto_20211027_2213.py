# Generated by Django 3.2.7 on 2021-10-27 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_review_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]