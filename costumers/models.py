from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class costumer_model(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to="costumers", default="def_costumer.png")
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    aadhar = models.IntegerField(blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    adress = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
