from django.urls import path
from images.api import views 

app_name = 'images'

urlpatterns = [
    path('listsss/', views.image_list_view),
    path('image_list/', views.image_list),
    path('<slug>/', views.image_list_detail, name='detail'),
    path('image_list/create', views.post_image_list, name='create'),
    path('image_list/<slug>/delete', views.image_list_delete, name='my_image_list_del'),    
]