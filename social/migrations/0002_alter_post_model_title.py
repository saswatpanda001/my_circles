# Generated by Django 3.2 on 2021-04-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='title',
            field=models.CharField(default='no-title', max_length=50),
        ),
    ]
