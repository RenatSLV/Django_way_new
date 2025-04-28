from django import forms

class BBCodeForm(forms.Form):
    bbcode_input = forms.CharField(widget=forms.Textarea, label="Введите BBCode")
