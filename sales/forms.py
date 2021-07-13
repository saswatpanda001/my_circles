from django import forms
from django.db.models import fields
from sales.models import Position, Sales

CHART_CHOICES = (
    ("#1", "BAR CAHRT"),
    ("#2", "PIE CHART"),
    ("#3", "LINE CHART")
)


class sales_search(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)


class sales_form(forms.ModelForm):
    class Meta():
        model = Sales
        fields = ("costumer", "positions")


class position_form(forms.ModelForm):
    class Meta():
        model = Position
        fields = ("product", "quantity")
