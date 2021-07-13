from django.db import models
from profiles.models import Profile_Model

class Report_Model(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="reports", default="def_report.jpg")
    remarks =models.TextField(blank=True,null=True)
    author = models.ForeignKey(Profile_Model, on_delete=models.CASCADE)

    def __str__(self):
      return self.name
