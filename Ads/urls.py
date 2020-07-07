from django.urls import path
from . import views


app_name= 'Ads'

urlpatterns = [
    path('', views.ad_view, name='ad_home'),
    path('pricing/', views.pricing_view, name='pricing'),
]