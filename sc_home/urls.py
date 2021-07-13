from django.urls import path
from sc_home import views

urlpatterns = [
    path("", views.welcome)
]