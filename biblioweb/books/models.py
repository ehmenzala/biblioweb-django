from django.db import models


class Author(models.Model):

    GENDER_MALE = "M"
    GENDER_FEMALE = "F"

    GENDER_CHOICES = [
        (None, "Género"),
        (GENDER_MALE, "Masculino"),
        (GENDER_FEMALE, "Femenino"),
    ]

    name = models.CharField(max_length=75)
    surname = models.CharField(max_length=75)
    gender = models.CharField(
        max_length=9,  blank=False, choices=GENDER_CHOICES)
    avatar = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(db_default='No description')

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=125)
    language = models.CharField(max_length=125)
    org_language = models.CharField('orginal lanugage', max_length=125)
    pub_year = models.IntegerField()
    pages = models.IntegerField()
    rating = models.IntegerField(db_default=0)
    description = models.TextField(db_default='No description')
    blurb = models.TextField(db_default='No blurb')
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)


class Cover(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    alt = models.CharField('alt text', max_length=255)
    path = models.FilePathField()


class Award(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=125)
