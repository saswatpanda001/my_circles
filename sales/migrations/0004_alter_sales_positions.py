# Generated by Django 3.2 on 2021-04-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_sales_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='positions',
            field=models.ManyToManyField(blank=True, to='sales.Position'),
        ),
    ]
