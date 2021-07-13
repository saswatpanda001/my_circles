from django.contrib import admin
from sales import models

admin.site.register(models.CSV)
admin.site.register(models.Position)
admin.site.register(models.Sales)


