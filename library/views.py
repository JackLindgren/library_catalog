import csv, io
from datetime import datetime

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Author, Book, Country, Language


YMD_FORMAT = "%Y-%m-%d"


class AuthorListView(generic.ListView):
    template_name = 'library/authors.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.order_by('last_name')


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'


def home_page(request):
    return render(request, 'library/home.html')


def books_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'library/author_books.html', context)


def add_author(request):
    if request.method == 'POST':
        new_author = Author()
        new_author.first_name = request.POST['first_name']
        new_author.last_name = request.POST['last_name']
        new_author.birth_date = request.POST['birth_date']
        new_author.death_date = request.POST['death_date'] or None
        new_author.country = Country.objects.get(pk=request.POST['country'])
        new_author.save()
        return HttpResponseRedirect(reverse('library:authors'))
    else:
        countries = Country.objects.all()
        context = {'countries': countries}
        return render(request, 'library/add_author.html', context)


def add_book(request):
    if request.method == 'POST':
        new_book = Book()
        new_book.title = request.POST['title']
        new_book.publication_date = request.POST['publication_date']
        new_book.author = Author.objects.get(pk=request.POST['author'])
        new_book.language = Language.objects.get(pk=request.POST['language'])
        new_book.save()
        # TODO: redirect to the author page
        return HttpResponseRedirect(reverse('library:authors'))
    else:
        languages = Language.objects.all()
        authors = Author.objects.order_by('last_name')
        context = {
            'languages': languages,
            'authors': authors
        }
        return render(request, 'library/add_book.html', context)


def upload_authors(request):
    if request.method == 'POST':
        author_file = request.FILES['author_file']
        author_data = author_file.read().decode('UTF-8')
        io_string = io.StringIO(author_data)
        reader = csv.DictReader(io_string)
        # TODO: validate the fieldnames
        # TODO: centralize the author creation logic - this is mostly the same as add_author()
        for row in reader:
            new_author = Author()
            new_author.first_name = row['first_name']
            new_author.last_name = row['last_name']
            new_author.birth_date = datetime.strptime(row['birth_date'], YMD_FORMAT).date()
            if row['death_date']:
                new_author.death_date = datetime.strptime(row['death_date'], YMD_FORMAT).date()
            new_author.country, created = Country.objects.get_or_create(country=row['country'])
            new_author.save()
        return HttpResponseRedirect(reverse('library:authors'))
    else:
        return render(request, 'library/author_upload.html')
