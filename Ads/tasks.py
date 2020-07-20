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

@periodic_task(run_every=crontab(minute=('*/1')))
def print_val():
    daily_ads = Ads.objects.filter(daily_ad=True)
    print ('celery is working well')
    for ads in daily_ads:
        if ads.expiry_date < datetime.now().date():
            print (f'expiry date = {ads.expiry_date}')
            print (f'the current date = {datetime.now().date()}')


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
