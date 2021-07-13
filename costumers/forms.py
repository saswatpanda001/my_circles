from django import forms
from costumers.models import costumer_model


class costumer_form(forms.ModelForm):
    class Meta():
        model = costumer_model
        fields = ('name', 'logo', 'city', 'state',
                  'aadhar', 'mobile', 'adress')
