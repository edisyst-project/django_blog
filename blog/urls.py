from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('about/', views.about, name='blog-about'),

    path('', views.post_list, name='blog-home'),  # Aggiorna la view qui
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/update/', views.post_update, name='post-update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),

]
