from django import forms

from App1.models import User
from App1.validators import validate_age, validator_name_length

class UserForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        label='Имя:',
        validators=[validator_name_length]
    )
    age = forms.IntegerField(
        label='Возраст',
        validators=[validate_age]
    )

    class Meta:
        model = User
        fields = ['name', 'age']
