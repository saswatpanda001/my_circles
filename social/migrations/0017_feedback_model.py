# Generated by Django 3.2 on 2021-04-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0016_userdt_model_following'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
