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
]