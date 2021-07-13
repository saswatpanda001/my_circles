import re
from django.contrib.auth.decorators import login_required
from django.db import models
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views import View
from django.shortcuts import render, redirect
from social.models import post_model, comment_model, userdt_model, feedback_model, messege_model, chat_model
from social.forms import post_form, comment_form, text_form
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from products.models import Product_Model
from django.urls import reverse_lazy

User = get_user_model()


@login_required
def post_view(request):
    if request.GET.get("query") != None:
        search_data = post_model.objects.filter(
            Q(title__icontains=request.GET.get("query")))
        return render(request, "search_post.html", {"data_sr": search_data, "search": "Search Posts"})

    x = post_model.objects.all().order_by("-created")
    return render(request, "post.html", {"data": x, "search": "Search Posts"})


@login_required
def mypost_view(request, pk):

    prod = Product_Model.objects.filter(author=pk)
    if request.GET.get("query") != None:
        search_data = userdt_model.objects.filter(
            Q(user__username__icontains=request.GET.get("query")))
        return render(request, "search_profile.html", {"data_sr": search_data, "search": "Search Profiles"})

    user_dt = userdt_model.objects.get(pk=pk)
    x = post_model.objects.filter(author=user_dt.user).order_by("-created")

    data_followers = user_dt.followers.all()
    data_following = user_dt.following.all()

    if request.user in data_followers:
        following = True

    else:
        following = False

    total_followers = len(data_followers)
    total_following = len(data_following)

    if request.method == "POST":

        if following == True:
            user_dt.followers.remove(request.user)
            # request.user.userdt_model.following.remove(user_dt.user)

            return redirect("social:profile", pk=user_dt.pk)
        if following == False:
            user_dt.followers.add(request.user)
            # request.user.userdt_model.following.add(user_dt.user)

            return redirect("social:profile", pk=user_dt.pk)

    pass_dict = {"data": x, "details": user_dt,
                 "is_fol": following, "tot_followers": total_followers,
                 "tot_following": total_following, "followers": data_followers,
                 "following": data_following, "pr_data": prod, "search": "Search Profiles"}

    return render(request, "profile.html", pass_dict)


@login_required
def postdetail_view(request, pk):
    liking = None
    nu_like = 0
    c = comment_model.objects.filter(com_id=pk).order_by("-created")
    y = comment_form(request.POST or None)

    if request.method == "POST" and "comment1_button" in request.POST:
        if y.is_valid() and y.cleaned_data.get("body") != None:
            z = comment_model.objects.create(
                body=y.cleaned_data.get("body"),
                com_id=pk,
                author=request.user,
            )
            z.save()
            return redirect("social:post_detail", pk=pk)

    x = post_model.objects.get(id=pk)
    likes = x.likes.all()
    nu_like = len(likes)
    if request.user in likes:
        liking = True
    else:
        liking = False

    if request.method == "POST" and "like_button" in request.POST:
        if liking == True:
            x.likes.remove(request.user)
            likes = x.likes.all()
            nu_like = len(likes)

        if liking == False:
            x.likes.add(request.user)
            likes = x.likes.all()
            nu_like = len(likes)

    likes = x.likes.all()
    nu_like = len(likes)
    if request.user in likes:
        liking = True
    else:
        liking = False

    p_user = post_model.objects.get(id=pk).author.id

    pass_data = {"data": x, "form": y, "com_data": c,
                 "like": liking, "tot_like": nu_like, 'p_user': p_user}

    return render(request, "details.html", pass_data)


@method_decorator(login_required, name='dispatch')
class postform_view(CreateView):
    model = post_model
    fields = ("title", "blog", "image")
    template_name = "post_form.html"
    context_object_name = "form"
    success_url = reverse_lazy('social:wall')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class post_editview(UpdateView):
    model = post_model
    fields = ("title", "blog", "image",)
    template_name = "update_post.html"
    context_object_name = "form"
    pk_url_kwarg = "pk"

    def get_success_url(self):

        companyid = self.kwargs['pk']
        return reverse_lazy('social:post_detail', kwargs={'pk': companyid})


@method_decorator(login_required, name='dispatch')
class profile_updateview(UpdateView):
    model = userdt_model
    fields = ("name", "date_of_birth", "city", "country", "bio", "image")
    template_name = "update_profile.html"
    context_object_name = "form"
    pk_url_kwarg = "pk"

    def get_success_url(self):
        companyid = self.kwargs['pk']
        return reverse_lazy('social:profile', kwargs={'pk': companyid})


@method_decorator(login_required, name='dispatch')
class post_deleteview(DeleteView):
    model = post_model
    template_name = "delete_post.html"
    pk_url_kwarg = 'pk'
    context_object_name = "data"

    def get_success_url(self):
        companyid = self.request.user.pk
        return reverse_lazy('social:profile', kwargs={'pk': companyid})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        userdt_model.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.userdt_model.save()


@method_decorator(login_required, name='dispatch')
class feedback_view(CreateView):
    model = feedback_model
    fields = "__all__"
    template_name = "feedback.html"
    success_url = reverse_lazy("social:greetings")
    context_object_name = "form"


@login_required
def greetings_view(request):
    return render(request, "greetings.html", {})


@login_required
def text_view(request, pk):
    details = {
        "send": int(str(request.user.pk)+str(pk)),
        "rec": int(str(pk)+str(request.user.pk)),
        "sender": request.user,
        "reciever": User.objects.get(id=pk),
    }

    s = int(str(request.user.pk)+str(pk))
    r = int(str(pk)+str(request.user.pk))

    x = messege_model.objects.filter(send=r)
    y = messege_model.objects.filter(send=s)
    z = x.union(y).order_by("-date")

    return render(request, "text.html", {"data": z, "details": details})


@login_required
def send_view(request, pk):
    details = {
        "send": int(str(request.user.pk)+str(pk)),
        "rec": int(str(pk)+str(request.user.pk)),
        "sender": request.user,
        "reciever": User.objects.get(id=pk),
    }

    form = text_form(request.POST or None)

    if request.method == "POST":
        if (request.POST['body'] != None):

            z = messege_model.objects.create(
                body=request.POST['body'],
                send=details["send"],
                rec=details["rec"],
                sender=details["sender"],
                reciever=details["reciever"],
                vip=str(details["sender"]),

            )
            z.save()
    return HttpResponse("Message sent")


@login_required
def get_mes(request, pk):

    s = int(str(request.user.pk)+str(pk))
    r = int(str(pk)+str(request.user.pk))

    x = messege_model.objects.filter(send=r)
    y = messege_model.objects.filter(send=s)

    z = x.union(y).order_by("-date")

    return JsonResponse({"messages": list(z.values())})


@login_required
def msglist_view(request):
    return render(request, "message.html")


@login_required
def index(request):
    return render(request, 'room_name.html', {})


@login_required
def room(request, room_name):

    if request.method == "POST":
        x = chat_model.objects.create(
            author=request.user,
            body=request.POST.get("body"),
            room_name=room_name,
        )
        x.save()
    x = chat_model.objects.filter(room_name=room_name).order_by("-cr_time")

    return render(request, 'room.html', {'room_name': room_name, "message_list": x})
