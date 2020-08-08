from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from Ads.models import Ads
from datetime import datetime

# Create your models here.
#creating a related profile to your user
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    occupation = models.CharField(max_length=30, null=False, default='unemployed')
    otherSkill = models.CharField(max_length=15, blank=True)
    monthly_ad = models.BooleanField(default=False)
    monthly_expiry = models.DateField(null=True, blank=True)
    yearly_ad = models.BooleanField(default=False)
    yearly_expiry = models.DateField(null=True, blank=True)


    def __str__(self):
        return f'Profile for user { self.user.username }'

#model for following users
class Contact(models.Model):
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

#adds the following field to user dynamically
user_model = get_user_model()
user_model.add_to_class('following', models.ManyToManyField('self', through=Contact,related_name='followers', symmetrical=False ))


# function that collects a signal from the ads app and updates the profile ad
def update_profile(sender, **kwargs):
    print(kwargs['instance'].user.username)
    if kwargs['instance'].monthly_ad == True:
        profile = Profile.objects.get(user=kwargs['instance'].user)
        # logic to set the profile monthly expiry to the users ad monthly expiry date
        if profile.monthly_expiry is None:
            profile.monthly_expiry = kwargs['instance'].expiry_date
        profile.monthly_ad = True
        print(profile.monthly_ad)
        profile.save()
    elif kwargs['instance'].yearly_ad == True:
        profile = Profile.objects.get(user=kwargs['instance'].user)
        # logic to set the profile monthly expiry to the users ad monthly expiry date
        if profile.yearly_expiry is None:
            profile.yearly_expiry = kwargs['instance'].expiry_date
        profile.yearly_ad = True
        profile.save()

# using post_save to send signal to the profile
post_save.connect(update_profile, sender=Ads)