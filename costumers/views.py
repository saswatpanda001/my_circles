from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from costumers.models import costumer_model
from costumers.forms import costumer_form
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q


@login_required
def home(request):

    if request.GET.get("query") != None:
        search_data = costumer_model.objects.filter(
            Q(name__icontains=request.GET.get("query")))
        search_data = search_data.filter(
            author=request.user)
        return render(request, "search_costumer.html", {"data_sr": search_data, "search": "Search Costumers"})

    costm = costumer_model.objects.filter(
        author=request.user).order_by("-created")
    return render(request, "home.html", {"data": costm, "search": "Search Costumers"})


@login_required
def create_costumer(request):
    form = costumer_form(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            cl_data = form.cleaned_data

            x = costumer_model.objects.create(
                name=cl_data.get("name"),
                logo=cl_data.get("logo"),
                author=request.user,

            )
            x.save()
            return redirect("/costumer")
    return render(request, "costumer_form.html", {"form": form})


@method_decorator(login_required, name='dispatch')
class costumer_updateview(UpdateView):
    model = costumer_model
    fields = ('name', 'logo', 'city', 'state',
              'aadhar', 'mobile', 'adress')
    template_name = "update.html"
    context_object_name = "form"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy('costumers:home')


@method_decorator(login_required, name='dispatch')
class costumer_deleteview(DeleteView):
    model = costumer_model
    template_name = "delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy('costumers:home')
