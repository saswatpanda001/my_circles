from django import forms
from django.forms import ModelForm, DateInput
from social import models


class post_form(forms.ModelForm):
    class Meta():

        model = models.post_model
        fields = ("title", "blog", "image",)


class comment_form(forms.ModelForm):
    class Meta():

        model = models.comment_model
        fields = ('body',)


class feedback_form(forms.ModelForm):
    class Meta():
        model = models.feedback_model
        fields = "__all__"


class text_form(forms.ModelForm):
    class Meta():
        model = models.messege_model
        fields = ('body', 'send', 'rec', 'sender', 'reciever',)


