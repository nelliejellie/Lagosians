from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import datetime as dt
from django.urls import reverse

# Create your models here.
CATEGORY_CHOICES = ( 
    ("jobs", "jobs"), 
    ("pets", "pets"), 
    ("services", "services"), 
    ("real estate", "real estate"), 
    ("vehicles", "vehicles"), 
    ("fashion", "fashion"), 
    ("products", "products"), 
)


class Ads(models.Model):
    category = models.CharField( 
        max_length = 20, 
        choices = CATEGORY_CHOICES, 
        default = 'jobs'
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    ad_image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    ad_image_two = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    created =  models.DateField(default=datetime.now, db_index=True)
    expiry_date = models.DateField()
    

    def __str__(self):
        return self.ad_name
    
    def get_absolute_url(self):
        return reverse('Ads:detail', args=[self.id, self.slug])


   

