from django.contrib import admin

from .models import Author, Book, Genre, Cover, Award

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Cover)
admin.site.register(Award)
