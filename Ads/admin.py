from django.contrib import admin
from .models import Ads

# Register your models here.

admin.site.register(Ads)

class AdsAdmin(admin.ModelAdmin):
    list_display = ['ad_name', 'user']
    prepopulated_fields = {'slug':('ad_name')}