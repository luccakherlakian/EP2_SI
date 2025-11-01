from django.urls import path
from . import views

# Estes nomes (ex: 'post_list') são os que usamos nos templates
urlpatterns = [
    # Rota para a lista de posts (página inicial)
    path('', views.post_list, name='post_list'),

    # Rota para o detalhe do post
    # <int:pk> captura o ID do post (Primary Key) da URL
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]