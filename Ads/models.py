from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import datetime as dt
from django.urls import reverse
from django.utils.text import slugify


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
        )
    user = models.ForeignKey(User, related_name='ads', on_delete=models.CASCADE)
    adname = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique_for_date='created')
    description = models.TextField()
    ad_image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    ad_image_two = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    daily_ad = models.BooleanField(default=False)
    weekly_ad = models.BooleanField(default=False)
    monthly_ad = models.BooleanField(default=False)
    yearly_ad = models.BooleanField(default=False)
    created =  models.DateField(default=datetime.now, db_index=True)
    expiry_date = models.DateField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.adname) # set the slug explicitly
        super(Ads, self).save(*args, **kwargs) # call Django's save()

    def __str__(self):
        return self.adname
    
    def get_absolute_url(self):
        return reverse('Ads:details', args=[self.id, self.slug])





   

