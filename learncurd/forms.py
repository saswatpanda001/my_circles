from django import forms
from learncurd import models

class post_form(forms.ModelForm):
    class Meta:
        model = models.demo_model
        fields = "__all__"
            