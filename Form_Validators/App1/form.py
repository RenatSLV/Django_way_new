from django import forms
from django.core.exceptions import ValidationError

from App1.models import Book

def value_less_0(value):
    if value <= 0:
        raise ValidationError('Значение не может быть меньше нуля или быть равно 0')
    
def value_length_0(value):
    if len(value) == 0:
        raise ValidationError('Поле не может быть пустым')

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=100, validators=[value_length_0])
    author = forms.CharField(max_length=100, validators=[value_length_0])
    price = forms.IntegerField(validators=[value_less_0])

    class Meta:
        model = Book
        fields = ['title', 'author', 'price']