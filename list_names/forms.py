from django import forms
from django.forms import ModelForm
from .models import ListNames


class ListNamesForm(ModelForm):
    name = forms.CharField(label='Add the name')

    class Meta:
        model = ListNames
        fields = ['name']
