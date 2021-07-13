from django.shortcuts import redirect, render
from products.forms import product_form, prod_comm, order_search, sales_search
from products.models import Product_Model, cart_model, product_comment, order_model, sales_list
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView, CreateView
from django.utils.decorators import method_decorator
from django.urls.base import reverse_lazy
from django.db.models import Q


@method_decorator(login_required, name='dispatch')
class create_product(CreateView):
    model = Product_Model
    fields = ("name", "image", "price", "bio")
    template_name = "products_form.html"
    context_object_name = "form"
    success_url = reverse_lazy('products:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def product_view(request):
    x = Product_Model.objects.filter(author=request.user).order_by("-created")

    if request.GET.get("query") != None:
        search_data = Product_Model.objects.filter(
            Q(name__icontains=request.GET.get("query")))
        search_data = search_data.filter(
            author=request.user).order_by("-created")

        return render(request, "search_product.html", {"data_sr": search_data, "search": "Search Products"})

    return render(request, "productlist.html", {"data": x, "search": "Search Products"})


@method_decorator(login_required, name='dispatch')
class product_updateview(UpdateView):
    model = Product_Model
    fields = ("name", "image", "price", "bio")
    template_name = "pr_update.html"
    context_object_name = "form"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy('products:home')


@method_decorator(login_required, name='dispatch')
class product_deleteview(DeleteView):
    model = Product_Model
    template_name = "pr_delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy('products:home')


@login_required
def prod_list(request):

    if request.GET.get("query") != None:
        search_data = Product_Model.objects.filter(
            Q(name__icontains=request.GET.get("query")))
        return render(request, "search_product1.html", {"data_sr": search_data, "search": "Search Products"})

    x = Product_Model.objects.all().order_by("-created")
    return render(request, "products.html", {"data": x, "search": "Search Products"})


@login_required
def products_details(request, pk):
    x = Product_Model.objects.get(id=pk)

    c = product_comment.objects.filter(com_id=pk).order_by("-created")
    len_com = len(c)
    net = 0
    y = prod_comm(request.POST or None)

    if request.method == "POST" and "comment_button" in request.POST:
        if y.is_valid() and y.cleaned_data.get("body") != None:
            z = product_comment.objects.create(
                body=y.cleaned_data.get("body"),
                com_id=pk,
                author=request.user,
            )
            z.save()
            return redirect('products:pr_details', pk=pk)

    if request.method == "POST" and "cart_button" in request.POST:

        if request.POST.get("quantity") != None:
            quantt = request.POST.get("quantity")
            net = int(x.price)*int(quantt)

            cart_mod = cart_model.objects.create(
                quantity=quantt,
                net_price=net,
                image=x.image,
                buyer=request.user,
                name=x,
                seller=x.author,
            )

            cart_mod.save()

            return redirect('products:cart')

    return render(request, "pr_details.html", {"data": x, "product_comm": c, "len_com": len_com})


@login_required
def cart_view(request):
    x = cart_model.objects.filter(buyer=request.user)
    y = len(x)

    sum_total = 0
    pr_collect = cart_model.objects.filter(buyer=request.user)
    for each in pr_collect:
        sum_total += each.net_price

    if request.method == "POST":

        salesman = []

        for each in x:
            if each.name.author not in salesman:
                salesman.append(each.name.author)
            ord_mod = order_model.objects.create(
                quantity=each.quantity,
                buyer=each.buyer,
                seller=each.seller,
                name=each.name,
                image=each.image,
                net_price=each.net_price,
            )

            ord_mod.save()

        for i in salesman:
            a = cart_model.objects.filter(seller=i)
            b = order_model.objects.all().order_by('-id')[:y][::-1]
            lii = []
            for each in b:
                if each.seller == i:
                    lii.append(each)

            print(b)
            summ = 0
            for each in a:
                summ += each.net_price

            sale = sales_list.objects.create(
                costumer=request.user,
                salesman=i,
                net_price=0,

            )
            summ = 0
            for each in a:
                summ += each.net_price
            for each in lii:
                sale.products.add(each)

            sale.net_price = summ
            sale.save()

        cart_model.objects.filter(buyer=request.user).delete()

        return redirect("products:confirm")

    return render(request, "cart.html", {"data": x, "sum": sum_total, "num_cart": y})


@method_decorator(login_required, name='dispatch')
class cart_deleteview(DeleteView):
    model = cart_model
    template_name = "delete_cart.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy('products:cart')


@login_required
def confirm(request):
    return render(request, "order.html")


@login_required
def orders(request):

    z = order_search(request.POST or None)
    a = None
    if request.method == "POST":
        if z.is_valid():
            cl_data = z.cleaned_data

            date_to = cl_data.get("date_to")
            date_from = cl_data.get("date_from")
            chart_type = cl_data.get("chart_type")

            a = sales_list.objects.filter(
                created__range=[date_from, date_to])

            a = a.filter(costumer=request.user).order_by("-created")
    return render(request, "order_details1.html", {"form": z, "ord_table": a})


@login_required
def ord_details(request, pk):
    x = sales_list.objects.get(transaction_id=pk)
    return render(request, "order_details2.html", {"data": x})


@login_required
def sales(request):
    z = sales_search(request.POST or None)
    a = None

    if request.method == "POST":
        if z.is_valid():
            cl_data = z.cleaned_data

            date_to = cl_data.get("date_to")
            date_from = cl_data.get("date_from")
            chart_type = cl_data.get("chart_type")

            a = sales_list.objects.filter(
                created__range=[date_from, date_to])

            a = a.filter(salesman=request.user).order_by("-created")
    return render(request, "sale_details1.html", {"form": z, "ord_table": a})


@login_required
def sale_details(request, pk):
    x = sales_list.objects.get(transaction_id=pk)
    return render(request, "sale_details2.html", {"data": x})
