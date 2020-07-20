from django.urls import path
from . import views


app_name= 'Ads'

urlpatterns = [
    path('', views.ad_view, name='ad_home'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('ad_form/', views.ad_form, name='ad_form'),
    path('details/<int:id>/<slug:slug>', views.ad_detail, name='details'),
]