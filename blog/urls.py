from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),         # Nuova rotta per il dettaglio
    path('post/<int:pk>/update/', views.post_update, name='post-update'),  # Nuova rotta per la modifica
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),  # Nuova rotta per l'eliminazione
]
