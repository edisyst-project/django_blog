from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('about/', views.about, name='blog-about'),

    path('', views.home, name='blog-home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/edit/', views.post_update, name='post-update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),

    path('register/', views.register, name='register'),
    # path('login/', views.CustomLoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
