# Generated by Django 3.2.4 on 2021-07-08 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0031_alter_chat_model_cr_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messege_model',
            name='image',
        ),
    ]
