from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render
from .models import Book


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'books.html', {"books": books})


def book(request: HttpRequest, book_id: int) -> HttpResponse:
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("This book does not exist.")
    return render(request, 'book-detail.html', {"book": book})
