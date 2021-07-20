from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Author, Book


class AuthorListView(generic.ListView):
    template_name = 'library/authors.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.order_by('last_name')


def books_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'library/author_books.html', context)
