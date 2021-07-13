from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from learncurd.models import demo_model
from django.urls import reverse_lazy


class list_view(ListView):
    model = demo_model
    template_name = "list.html"
    context_object_name = "data"


class detail_view(DetailView):
    model = demo_model
    template_name = "detail.html"
    context_object_name = "data"
    pk_url_kwarg = "pk"


class create_view(CreateView):
    model = demo_model
    template_name = "create.html"
    fields = "__all__"
    success_url = reverse_lazy("learn:list")
    context_object_name = "form"


class edit_view(UpdateView):
    model = demo_model
    template_name = "create.html"
    fields = "__all__"
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy("learn:list")
    context_object_name = "form"


class delete_view(DeleteView):
    model = demo_model
    template_name = "delete.html"
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy("learn:list")
