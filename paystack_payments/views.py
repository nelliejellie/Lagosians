from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerInfo
from Ads.models import Ads
from django.contrib.auth.models import User

# Create your views here.
def customer_info(request):
    current_user = User.objects.get(id=request.user.id)
    context = {
            'payment_email': current_user.email,
            'payment_firstname': current_user.first_name,
            'payment_lastname': current_user.last_name
        }
    return render(request, 'paystack/payment.html', context)

def customer_info_monthly_pay(request):
    current_user = User.objects.get(id=request.user.id)
    context = {
            'payment_email': current_user.email,
            'payment_firstname': current_user.first_name,
            'payment_lastname': current_user.last_name
        }
    return render(request, 'paystack/payment_monthly.html', context)

def customer_info_yearly_pay(request):
    current_user = User.objects.get(id=request.user.id)
    context = {
            'payment_email': current_user.email,
            'payment_firstname': current_user.first_name,
            'payment_lastname': current_user.last_name
        }
    return render(request, 'paystack/payment_yearly.html', context)

