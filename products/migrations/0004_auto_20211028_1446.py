# Generated by Django 3.2.7 on 2021-10-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211028_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_product',
            name='review_comment',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review_product',
            name='review_title',
            field=models.CharField(default=True, max_length=1000),
        ),
    ]
