from django.contrib import admin
from products import models


admin.site.register(models.Product_Model)

admin.site.register(models.product_comment)
admin.site.register(models.cart_model)
admin.site.register(models.order_model)
admin.site.register(models.sales_list)
