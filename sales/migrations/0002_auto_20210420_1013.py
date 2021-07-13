# Generated by Django 3.2 on 2021-04-20 10:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_model_image'),
        ('costumers', '0003_alter_costumer_model_name'),
        ('products', '0002_auto_20210420_0652'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='csv',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='csv',
            name='filename',
            field=models.FileField(blank=True, null=True, upload_to='csvfiles'),
        ),
        migrations.AddField(
            model_name='csv',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='position',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='position',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product_model'),
        ),
        migrations.AddField(
            model_name='position',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='costumer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='costumers.costumer_model'),
        ),
        migrations.AddField(
            model_name='sales',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sales',
            name='net_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='positions',
            field=models.ManyToManyField(blank=True, to='sales.Position'),
        ),
        migrations.AddField(
            model_name='sales',
            name='salesman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile_model'),
        ),
        migrations.AddField(
            model_name='sales',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
