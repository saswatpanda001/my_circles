from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class demo_model(models.Model):

    blog = models.TextField(blank=True, null=True)
    title = models.CharField(
        max_length=50, default="no-title")
    image = models.ImageField(
        upload_to="lrn/", default="lrn/def_post.jpg")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('learn:detail', args=[self.pk])

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
