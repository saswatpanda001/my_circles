from django.db import models
from django import forms

from django.contrib.auth import get_user_model
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey

from django.utils import timezone

User = get_user_model()


class post_model(models.Model):

    blog = models.TextField(blank=True, null=True)
    title = models.CharField(
        max_length=50, default="no-title")
    image = models.ImageField(
        upload_to="posts/", default="posts/def_post.jpg", blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="dislike", blank=True)

    def __str__(self):
        return self.title


class comment_model(models.Model):
    body = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    com_id = models.IntegerField(blank=True, null=True)

    likes = models.ManyToManyField(User, related_name="com_like", blank=True)
    dislikes = models.ManyToManyField(
        User, related_name="com_dislike", blank=True)

    def __str__(self):
        return str(self.com_id)+str(self.author)


class userdt_model(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=40,  blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=130, blank=True, null=True)
    image = models.ImageField(
        upload_to="social_profile", default="social_profile/def_profile.png", blank=True)

    followers = models.ManyToManyField(
        User, related_name="followers", blank=True)

    following = models.ManyToManyField(
        User, related_name="following", blank=True)

    def __str__(self):
        return str(self.user)


class feedback_model(models.Model):
    title = models.CharField(max_length=50)
    feedback = models.TextField()

    def __str__(self):
        return self.title


class messege_model(models.Model):
    send = models.IntegerField(blank=True, null=True)
    rec = models.IntegerField(blank=True, null=True)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="+")
    reciever = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="+")
    vip = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=500, blank=True, null=True)

    date = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)


class chat_model(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.CharField(max_length=250, blank=True, null=True)
    cr_time = models.DateTimeField(default=timezone.now, blank=True, null=True)
    room_name = models.CharField(max_length=250, blank=True, null=True)

    def render_text(self):
        x = chat_model.objects.all().order_by("-cr_time")
        if len(x) > 51:
            return x[0:50]
        else:
            return x

    def __str__(self):
        return str(self.author)+"-"+"ROOM:"+str(self.room_name)
