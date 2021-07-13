import re
from django.http import request
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from sales.models import Sales, Position
from sales.forms import sales_search, sales_form, position_form
from sales.utils import generate_id, get_costumer, get_salesman
import pandas as pd


@login_required
def home_view(request):

    form = sales_search(request.POST or None)
    sales_df = None
    position_data = []
    positions_df = None
    merge_df = None
    grp_df = []
    if request.method == "POST":

        if form.is_valid():
            cl_data = form.cleaned_data

            date_to = cl_data.get("date_to")
            date_from = cl_data.get("date_from")
            chart_type = cl_data.get("chart_type")

            a = Sales.objects.filter(
                created__range=[date_from, date_to])
            a = a.filter(salesman=request.user.pk)
            if len(a) > 0:
                sales_df = pd.DataFrame(a.values())

                # sales_df.rename(
                #     {'salesman_id': 'salesman', 'costumer_id': 'costumer', 'id': 'Product_ID'}, axis=1, inplace=True)

                # sales_df["created"] = sales_df["created"].apply(
                #     lambda x: x.strftime('%Y-%m-%d'))

                # sales_df["id"] = sales_df["sale_id"]
                # sales_df["costumer"] = sales_df["costumer"].apply(
                #     get_costumer)
                # sales_df["salesman"] = sales_df["salesman"].apply(get_salesman)

            for each in a:
                for data in each.get_positions():
                    if data.author == request.user:

                        obj = {
                            "Product_ID": data.id,
                            "Transaction_id": data.get_sales_id(),
                            "Product_Name": data.product,

                            "Quantity": data.quantity,
                            "Price": data.price,
                            "sold_on": data.created,
                        }
                        position_data.append(obj)

            sales_df = sales_df.to_html()
            positions_df = pd.DataFrame(position_data)

            positions_df = positions_df.to_html()

            # if len(position_data) > 0:
            #     positions_df = pd.DataFrame(position_data.values())
            #     merge_df = pd.DataFrame.merge(
            #         sales_df, positions_df, on="Product_ID")
            #     grp_df = merge_df.groupby("Transaction_id", as_index=False)[
            #         "Price"].agg("sum")

            #     merge_df = merge_df.to_html()
            #     positions_df = positions_df.to_html()
            #     grp_df = grp_df.to_html(), "merge_df": merge_df, "grp_df": grp_df

    data_dict = {"forms": form,
                 "sales_df": sales_df, "positions_df": positions_df}
    return render(request, "sales_home.html", {"data_dict": data_dict})


@login_required
def sales_listview(request):
    a = Sales.objects.filter(salesman=request.user).order_by("-created")
    return render(request, "sales_list.html", {"data": a})


@method_decorator(login_required, name='dispatch')
class sales_detailview(DetailView):
    model = Sales
    template_name = "sales_detail.html"
    context_object_name = "data"


@login_required
def sales_formview(request):
    form = sales_form(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            cl_data = form.cleaned_data
            pri = 0
            for each in cl_data.get("positions"):
                pri += each.price

            x = Sales.objects.create(
                costumer=cl_data.get("costumer"),
                salesman=request.user,
                transaction_id=generate_id(),
                net_price=pri,

            )
            for each in cl_data.get("positions"):
                x.positions.add(each)
            x.save()
            return redirect("/sales")

    return render(request, "sales_form.html", {"form": form})


@login_required
def create_positions(request):
    form = position_form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            clean = form.cleaned_data

            x = Position.objects.create(
                product=clean.get("product"),
                quantity=clean.get("quantity"),
                price=clean.get("product").price * clean.get("quantity"),
                author=request.user,
            )
            x.save()
            return redirect("/sales")
    return render(request, "position_form.html", {"form": form})
