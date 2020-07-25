from django.urls import path
from . import views


app_name= 'paystack_payments'

urlpatterns = [
    path('payment/', views.customer_info, name='payment'),
]