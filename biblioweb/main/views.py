from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from biblioweb.books.models import Book


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'index.html', {"books": books})
