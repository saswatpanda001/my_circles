# Generated by Django 3.2 on 2021-06-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0021_alter_userdt_model_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='image',
            field=models.ImageField(blank=True, default='posts/def_post.jpg', upload_to='posts/'),
        ),
    ]
