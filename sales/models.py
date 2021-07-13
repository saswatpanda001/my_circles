from django.db import models
from products.models import Product_Model
from django.utils import timezone
from costumers.models import costumer_model
from profiles.models import Profile_Model
from sales.utils import generate_id
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class Position(models.Model):
    product = models.ForeignKey(
        Product_Model, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    price = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.price = self.quantity*self.product.price
        return super().save(*args, **kwargs)

    def get_sales_id(self):
        sale_obj = self.sales_set.first()
        return sale_obj.transaction_id

    def __str__(self):
        return f"id:{self.id} Product:{self.product} Quantity:{self.quantity} Price:{self.price}"


class Sales(models.Model):
    transaction_id = models.CharField(max_length=20, blank=True, null=True)
    net_price = models.FloatField(blank=True, null=True)
    costumer = models.ForeignKey(
        costumer_model, on_delete=models.CASCADE, blank=True, null=True)
    salesman = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    positions = models.ManyToManyField(
        Position, blank=True)
    created = models.DateField(default=timezone.now)

    def __str__(self):
        return f'id:{self.transaction_id}---price:{self.net_price}'

    def get_positions(self):
        return self.positions.all()

    def get_absolute_url(self):
        return reverse('sales:details', kwargs={'pk': self.pk})


class CSV(models.Model):
    filename = models.FileField(upload_to='csvfiles', blank=True, null=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.filename
