from django import template
from ..models import Contact
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

register = template.Library()

@register.simple_tag
def followers(user=User):
    pass