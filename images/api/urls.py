from django.urls import path
from images.api import views

app_name = 'images'

urlpatterns = [
    path('image_list/', views.image_list),
]