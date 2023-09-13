# ratings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rating_list, name='rating_list'),
    path('create/', views.create_rating, name='create_rating'),
    path('update/<int:pk>/', views.update_rating, name='update_rating'),
    path('delete/<int:pk>/', views.delete_rating, name='delete_rating'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_movie/', views.create_movie, name='create_movie'),
    path('rating_list/', views.rating_list, name='rating_list'),
]

