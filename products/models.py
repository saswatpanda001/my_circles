import uuid
from django.db import models
from django.db.models.fields import related
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Product_Model(models.Model):
    name = models.CharField(max_length=110, blank=True, null=True)
    image = models.ImageField(upload_to="products", default="def_product.jpg")
    bio = models.TextField(blank=True, null=True)
    price = models.FloatField(help_text="in rupees", blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class product_comment(models.Model):
    body = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="prd_com")
    created = models.DateTimeField(default=timezone.now)
    com_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.com_id)+str(self.author)


class cart_model(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="br")
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='slr')
    net_price = models.FloatField(blank=True, null=True)
    name = models.ForeignKey(
        Product_Model, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="cart", default="def_product.jpg")

    def __str__(self):
        return str(self.seller)+" "+str(self.name)+" "+str(self.net_price)


class order_model(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="buyer")
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="seller")
    net_price = models.FloatField(blank=True, null=True)
    name = models.ForeignKey(
        Product_Model, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="cart", default="def_product.jpg")

    def __str__(self):
        return str(self.seller)+" "+str(self.name)+" "+str(self.net_price)


class sales_list(models.Model):
    transaction_id = models.CharField(max_length=20, blank=True, null=True)
    net_price = models.FloatField(blank=True, null=True)
    costumer = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="sale_costumer")
    salesman = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="sale_owner")
    products = models.ManyToManyField(
        order_model, blank=True)
    created = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.transaction_id == None:
            self.transaction_id = str(
                uuid.uuid4()).replace("-", "")[:10].upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.salesman)
