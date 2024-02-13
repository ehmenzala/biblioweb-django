from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.book, name='detail'),
    path('genre/<int:genre_id>/', views.genre, name='genre'),
]
