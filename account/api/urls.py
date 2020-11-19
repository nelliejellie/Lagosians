from django.urls import path
from account.api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('login', obtain_auth_token, name='login'),
    path('properties', views.account_properties_view, name='properties'),
    path('properties/update', views.account_properties_view, name='update'),
    path('register/', views.registeration_view, name='api_register'),
]