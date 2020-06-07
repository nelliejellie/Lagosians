from django.contrib import admin
from .models import Profile,Contact



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth')
    

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to',)

   


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact, ContactAdmin)