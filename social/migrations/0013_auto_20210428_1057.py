# Generated by Django 3.2 on 2021-04-28 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0012_auto_20210428_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdt_model',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userdt_model',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userdt_model',
            name='image',
            field=models.ImageField(blank=True, default='def_profile.png', upload_to='social_profile'),
        ),
        migrations.AlterField(
            model_name='userdt_model',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userdt_model',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
