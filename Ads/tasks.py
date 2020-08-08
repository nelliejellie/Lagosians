from celery import shared_task
from celery import task
from celery.task import periodic_task
from celery.schedules import crontab
from django.utils import timezone
from datetime import datetime
from .models import Ads
from django.core.mail import send_mail
from account.models import Profile


#task to filter daily ads
@periodic_task(run_every=crontab(minute=('*/5')))
def delete_daily_ads():
    #filter all ads by daily ads
    daily_ads = Ads.objects.filter(daily_ad=True)
    for ads in daily_ads:
        if ads.expiry_date < datetime.now().date():
            print (f'{ads} is greater than expiry date')
            ads.delete()
    return f'daily ads has been deleted at {timezone.now()}'

#task to filter weekly ads
@periodic_task(run_every=crontab(minute=('*/5')))
def delete_weekly_ads():
    #filter all ads by daily ads
    weekly_ads = Ads.objects.filter(weekly_ad=True)
    for ads in weekly_ads:
        if ads.expiry_date < datetime.now().date():
            print (f'{ads} is greater than expiry date')
            ads.delete()
    return f'daily ads has been deleted at {timezone.now()}'

#task to filter monthly ads
@periodic_task(run_every=crontab(minute=('*/5')))
def delete_monthly_ads():
    #filter all ads by daily ads
    monthly_ads = Ads.objects.filter(monthly_ad=True)
    for ads in monthly_ads:
        if ads.expiry_date < datetime.now().date():
            print (f'{ads} is greater than expiry date')
            ads.delete()
    return f'daily ads has been deleted at {timezone.now()}'

#task to filter yearly ads
@periodic_task(run_every=crontab(minute=('*/5')))
def delete_yearly_ads():
    #filter all ads by daily ads
    yearly_ads = Ads.objects.filter(yearly_ad=True)
    for ads in  yearly_ads:
        if ads.expiry_date < datetime.now().date():
            print (f'{ads} is greater than expiry date')
            ads.delete()
    return f'daily ads has been deleted at {timezone.now()}'

# task  for sending email for daily ads
@task
def daily_ad_posted(ad_id):
    ads = Ads.objects.get(id=ad_id)
    #create invoice e-mail
    subject = f'{ads.user.first_name} {ads.user.last_name} Daily Ad'
    message =  'Your daily advert has been created'
    mail_sent = send_mail(subject, message, 'admin@lagosians.com',[ads.user.email])
    print(f' print = {mail_sent}')
    #send e-mail
    return mail_sent

# task  for sending email for weekly ads
@task
def weekly_ad_posted(ad_id):
    ads = Ads.objects.get(id=ad_id)
    #create invoice e-mail
    subject = f'{ads.user.first_name} {ads.user.last_name} Daily Ad'
    message =  'Your weekly advert has been created'
    mail_sent = send_mail(subject, message, 'admin@lagosians.com',[ads.user.email])
    print(f' print = {mail_sent}')
    #send e-mail
    return mail_sent

# task  for sending email for monthly ads
@task
def monthly_ad_posted(ad_id):
    ads = Ads.objects.get(id=ad_id)
    #create invoice e-mail
    subject = f'{ads.user.first_name} {ads.user.last_name} Daily Ad'
    message =  'Your monthly advert has been created'
    mail_sent = send_mail(subject, message, 'admin@lagosians.com',[ads.user.email])
    print(f' print = {mail_sent}')
    #send e-mail
    return mail_sent

# task for sending email for yearly ads
@task
def yearly_ad_posted(ad_id):
    ads = Ads.objects.get(id=ad_id)
    #create invoice e-mail
    subject = f'{ads.user.first_name} {ads.user.last_name} Daily Ad'
    message =  'Your yearly advert has been created'
    mail_sent = send_mail(subject, message, 'admin@lagosians.com',[ads.user.email])
    print(f' print = {mail_sent}')
    #send e-mail
    return mail_sent