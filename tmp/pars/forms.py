from django import forms


class FoundForm(forms.Form):
    name = forms.CharField(label='Вакансия')


class MainForm(forms.Form):
    tmp = None
