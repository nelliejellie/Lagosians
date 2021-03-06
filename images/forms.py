from django import forms
from .models import Image,Comment
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'description','image')

class CommentForm(forms.ModelForm):
    class Meta:
        # assign a varibale to the model you want to create a form from
        model = Comment
        # the fields you want on the frontend
        fields = ('body', )


    