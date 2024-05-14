from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('authors/', views.authors, name='authors'),
    path('read/<slug:slug>/', views.read, name='read'),
    path('genre/<int:genre_id>/', views.genre, name='genre'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]
