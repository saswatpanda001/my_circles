# Generated by Django 3.2 on 2021-04-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_alter_post_model_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='image',
            field=models.ImageField(default='def_post.jpg', upload_to='posts/'),
        ),
    ]