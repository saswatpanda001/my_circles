# Generated by Django 3.2.4 on 2021-07-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_cart_model_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_model',
            name='net_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
