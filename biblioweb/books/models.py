from django.db import models


class Author(models.Model):

    GENDER_MALE = "M"
    GENDER_FEMALE = "F"

    GENDER_CHOICES = [
        (None, "Género"),
        (GENDER_MALE, "Masculino"),
        (GENDER_FEMALE, "Femenino"),
    ]

    name = models.CharField(verbose_name='Name', max_length=75)
    surname = models.CharField(verbose_name='Surname', max_length=75)
    gender = models.CharField(
        verbose_name='Gender', max_length=9,  blank=False, choices=GENDER_CHOICES)
    avatar = models.CharField(verbose_name='Avatar URL', max_length=255)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Genre(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    description = models.TextField(
        verbose_name='Description', db_default='No description')

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    isbn = models.CharField(verbose_name='ISBN', max_length=13)
    title = models.CharField(verbose_name='Title', max_length=125)
    language = models.CharField(verbose_name='Language', max_length=125)
    org_language = models.CharField(
        verbose_name='Original language', max_length=125)
    pub_year = models.IntegerField(verbose_name='Year of publication')
    pages = models.IntegerField(verbose_name='No. of pages')
    rating = models.IntegerField(verbose_name='Rating', db_default=0)
    description = models.TextField(
        verbose_name='Description', db_default='No description')
    blurb = models.TextField(verbose_name='Blurb', db_default='No blurb')
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return self.title


class Cover(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    alt = models.CharField(verbose_name='Alternative text', max_length=255)
    path = models.FilePathField(verbose_name='Image Path')


class Award(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name='Name', max_length=125)

    def __str__(self) -> str:
        return self.name
