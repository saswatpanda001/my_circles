# Generated by Django 3.2.4 on 2023-10-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20231013_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='image1',
            field=models.ImageField(default='def_product.jpg', upload_to='products'),
        ),
        migrations.AddField(
            model_name='product_model',
            name='image2',
            field=models.ImageField(default='def_product.jpg', upload_to='products'),
        ),
        migrations.AddField(
            model_name='product_model',
            name='image3',
            field=models.ImageField(default='def_product.jpg', upload_to='products'),
        ),
        migrations.AddField(
            model_name='product_model',
            name='image4',
            field=models.ImageField(default='def_product.jpg', upload_to='products'),
        ),
    ]
