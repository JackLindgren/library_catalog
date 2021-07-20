from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)


class Language(models.Model):
    language = models.TextField(max_length=30, unique=True)

    def __str__(self):
        return self.language


class Country(models.Model):
    country = models.TextField(max_length=30, unique=True)

    def __str__(self):
        return self.country


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    death_date = models.DateField(null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def count_books(self):
        return Book.objects.filter(author=self).count()


class Book(models.Model):
    title = models.CharField(max_length=100)
    # TODO: null=True should be removed eventually
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # TODO: add support for an arbitrary number of secondary authors
    publication_date = models.DateField()
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} ({self.publication_date.year})"


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_read = models.DateField()
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
