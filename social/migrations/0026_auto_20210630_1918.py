# Generated by Django 3.2.4 on 2021-06-30 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0025_auto_20210630_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messege_model',
            name='rec',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='messege_model',
            name='send',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]