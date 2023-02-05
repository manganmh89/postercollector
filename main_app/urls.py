from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('admin', views.admin, name='admin'),
    path('about/', views.about, name='about'),
    path('posters/', views.posters_index, name='index'),
    path('posters/<int:poster_id>/', views.posters_detail, name='detail'),
    path('posters/create/', views.PosterCreate.as_view(), name='posters_create'),
    path('posters/<int:pk>/update/', views.PosterUpdate.as_view(), name='posters_update'),
    path('posters/<int:pk>/delete/', views.PosterDelete.as_view(), name='posters_delete'),
    path('posters/<int:poster_id>/add_variation/', views.add_variation, name='add_variation'),
    path('dream/', views.DreamIndex.as_view(), name='dream_index'),
    path('dream/create', views.DreamCreate.as_view(), name='dream_create'),
    path('dream/<int:pk>/', views.DreamDetail.as_view(), name='dream_detail'),
    path('dream/<int:pk>/update/', views.DreamUpdate.as_view(), name='dream_update'),
    path('dream/<int:pk>/delete/', views.DreamDelete.as_view(), name='dream_delete'),

]