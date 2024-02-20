from django.http import HttpResponse, HttpRequest, Http404, HttpResponseBadRequest
from django.shortcuts import render
from .models import Book, Genre


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    genres = Genre.objects.all()
    context = {
        "books": books,
        "genres": genres
    }
    return render(request, 'books.html', context)


def detail(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404("This book does not exist.")
    return render(request, 'book-detail.html', {"book": book})


def genre(request: HttpRequest, genre_id: int) -> HttpResponse:
    genres = Genre.objects.all()
    books = Book.objects.filter(genres__id=genre_id)

    try:
        selected_genre = Genre.objects.get(pk=genre_id)
    except Genre.DoesNotExist:
        raise Http404("This genre does not exist.")

    context = {
        "books": books,
        "genres": genres,
        "selected_genre": selected_genre,
    }
    return render(request, 'book-genre.html', context)


def read(request: HttpRequest, slug: str) -> HttpResponse:
    page = request.GET.get('page')
    chapter = request.GET.get('chapter')

    if (page == None or chapter == None):
        return HttpResponseBadRequest('400. Bad Request: URL parameters are invalid.')

    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404("This book does not exist.")

    context = {
        "book": book,
        "chapter": chapter,
        "page": page
    }
    return render(request, 'book-read.html', context)
