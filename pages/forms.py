from django import forms
from images.models import Image
from urllib import request


class SearchForm(forms.Form):
    query = forms.CharField()