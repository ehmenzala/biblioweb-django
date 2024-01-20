from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # ex: /books/
    path('', views.index, name='index'),
    # ex: /books/5
    path('<int:book_id>/', views.book, name='detail'),
    # ex: /books/genre/1
    path('genre/<int:genre_id>/', views.genre, name='genre'),
]
