# Generated by Django 3.2.4 on 2021-06-30 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0027_auto_20210630_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messege_model',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dm_img/'),
        ),
    ]
