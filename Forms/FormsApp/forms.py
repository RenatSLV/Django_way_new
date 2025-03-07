from django.forms import ModelForm
from django import forms

from FormsApp.models import IceCream

class IceCreamForm(ModelForm):
    name = forms.CharField(label="Название мороженого")
    description = forms.CharField(label='Описание',
                                  widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена',
                               decimal_places=2)
    quantity = forms.IntegerField(label='Количество')

    class Meta:
        model = IceCream
        fields = ('name', 'description', 'price', 'quantity')
