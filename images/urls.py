from django.urls import path
from . import views

app_name= 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
    # url for the comment likes
    path('like_comment/', views.comment_like, name='like_comment'),
    path('', views.image_list, name='list'),
    # url for the ranking
    path('ranking/', views.image_ranking, name='ranking'),
]