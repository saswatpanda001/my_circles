from django.urls import path
from sales import views


app_name = 'sales'

urlpatterns = [
    path("", views.home_view),
    path("list/", views.sales_listview),
    path("<int:pk>/", views.sales_detailview.as_view(), name="details"),
    path("create_sale/", views.sales_formview, name="sale_data"),
    path("create_pos/", views.create_positions, name="pos"),
]
