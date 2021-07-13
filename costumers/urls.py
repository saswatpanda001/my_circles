from django.urls import path
from costumers import views


app_name = 'costumers'

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_costumer),
    path("update/<int:pk>", views.costumer_updateview.as_view(), name="update"),
    path("delete/<int:pk>", views.costumer_deleteview.as_view(), name="delete"),
]
