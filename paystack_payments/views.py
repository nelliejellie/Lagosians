from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerInfo
from Ads.models import Ads

# Create your views here.
def customer_info(request):
    payment_ads = Ads.objects.filter(user=request.user)
    for ad in payment_ads:
        print (ad.user.email)
        context = {
            'payment_email': ad.user.email,
            'payment_firstname': ad.user.first_name,
            'payment_lastname': ad.user.last_name
        }
    return render(request, 'paystack/payment.html', context)

