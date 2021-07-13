# Generated by Django 3.2 on 2021-04-28 14:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0013_auto_20210428_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdt_model',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userdt_model',
            name='bio',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]