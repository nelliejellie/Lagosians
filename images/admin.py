from django.contrib import admin
from .models import Image, Comment
from django.contrib.admin import AdminSite

#rename the admin header
admin.site.site_header = 'Lagosians'
    
# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','active', 'image', 'created',]
    list_filter = ['user', 'created']
    search_fields = ['email', 'body', 'user']
