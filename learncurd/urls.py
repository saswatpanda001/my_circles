from django.urls import path
from learncurd import views

app_name = "learn"


urlpatterns = [
    path("list", views.list_view.as_view(), name="list"),
    path("list/<int:pk>", views.detail_view.as_view(), name="detail"),
    path("create", views.create_view.as_view(), name="create"),
    path("list/<int:pk>/edit", views.edit_view.as_view(), name="edit"),
    path("list/<int:pk>/delete", views.delete_view.as_view(), name="delete"),

]
