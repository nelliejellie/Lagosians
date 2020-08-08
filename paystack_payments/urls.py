from django.urls import path
from . import views


app_name= 'paystack_payments'

urlpatterns = [
    path('payment/', views.customer_info, name='payment'),
    path('payment_monthly/', views.customer_info_monthly_pay, name='payment_monthly'),
    path('payment_yearly/', views.customer_info_yearly_pay, name='payment_yearly'),
]