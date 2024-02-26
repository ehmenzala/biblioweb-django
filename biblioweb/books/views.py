from django.conf import settings
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseBadRequest
from django.shortcuts import render
from .models import Book, Genre
from .utils import get_line_indices_for_paragraphs
from pathlib import Path


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
    page = int(request.GET.get('page', 1))
    chapter = int(request.GET.get('chapter', 1))

    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404("This book does not exist.")

    try:
        chapter_path = Path(
            settings.BASE_DIR /
            f'biblioweb/books/static/books/{book.slug}/ch{chapter}.txt'
        )
        with chapter_path.open() as chapter_file:
            chapter_content = ''
            raw_lines = chapter_file.readlines()
            lines = [line for line in raw_lines if line != '\n']
            paragraphs_indices = get_line_indices_for_paragraphs(page, lines)
            for i in paragraphs_indices:
                chapter_content += lines[i]
            chapter_file.close()

    except FileNotFoundError as err:
        print(f'File \'{err.filename}\' does not exists):')

    context = {
        "book": book,
        "chapter": chapter,
        "chapter_content": chapter_content,
        "page": page
    }
    return render(request, 'book-read.html', context)
