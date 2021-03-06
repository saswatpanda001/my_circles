# Generated by Django 3.2 on 2021-04-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0003_alter_costumer_model_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer_model',
            name='aadhar',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='costumer_model',
            name='adress',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='costumer_model',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='costumer_model',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='costumer_model',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
