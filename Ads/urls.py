from django.urls import path
from . import views


app_name= 'Ads'

urlpatterns = [
    path('', views.ad_view, name='ad_home'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('ad_form/', views.ad_form, name='ad_form'),
    path('ad_form_weekly/', views.ad_form_weekly, name='ad_form_weekly'),
    path('ad_form_monthly/', views.ad_form_monthly, name='ad_form_monthly'),
    path('ad_form_yearly/', views.ad_form_yearly, name='ad_form_yearly'),
    path('details/<int:id>/<slug:slug>', views.ad_detail, name='details'),
]