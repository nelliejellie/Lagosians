from django.contrib import admin
from .models import Ads

# Register your models here.

@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['adname', 'user', 'slug']
    prepopulated_fields = {'slug':('adname',)}