# Generated by Django 3.2 on 2021-04-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210420_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
