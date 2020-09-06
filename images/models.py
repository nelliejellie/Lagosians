from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now=True, db_index=True)
    #creating a manytomany relationship for image likes
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)
    total_likes = models.PositiveIntegerField(db_index=True, default=0)
    
    def __str__(self):
        return self.title

    #function to automatically generate image slug if none is provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='images_comment', on_delete=models.CASCADE)
    body = models.TextField()
    created =  models.DateField(default=datetime.now, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    like = models.ManyToManyField(User, related_name='comment_like')
    dislike = models.ManyToManyField(User, related_name='comment_dislike')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.user}\'s comment'

