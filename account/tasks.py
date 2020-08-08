from celery.task import periodic_task
from .models import Profile
from django.utils import timezone
from celery.schedules import crontab
from datetime import datetime


@periodic_task(run_every=crontab(minute=('*/5')))
def remove_monthly_subscription():
    #filter all ads by daily ads
    profile = Profile.objects.filter(monthly_ad=True)
    for prof in profile:
        if prof.monthly_expiry < datetime.now().date():
            prof.monthly_ad = False
    return f'monthly ads has been deleted at {timezone.now()}'

@periodic_task(run_every=crontab(minute=('*/5')))
def remove_yearly_subscription():
    #filter all ads by daily ads
    profile = Profile.objects.filter(yearly_ad=True)
    for prof in profile:
        if prof.yearly_expiry < datetime.now().date():
            prof.yearly_ad = False
    return f'yearly ads has been deleted at {timezone.now()}'