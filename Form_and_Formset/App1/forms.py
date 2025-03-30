from django import forms
from captcha.fields import CaptchaField

class AddClientForm(forms.Form):
    name = forms.CharField(label='Введите имя', max_length=50)
    age = forms.IntegerField(label='Введите возраст')
    captcha = CaptchaField(label='Введите текст для каптчи', error_messages={'invalid': 'неправильный текст'})
