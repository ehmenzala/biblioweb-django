from django.contrib import admin

from .models import Question, Choice, Author, Book, Genre, Cover, Award

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Cover)
admin.site.register(Award)
