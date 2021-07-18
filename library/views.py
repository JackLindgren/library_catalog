from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Author


class AuthorListView(generic.ListView):
    template_name = 'library/authors.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.order_by('last_name')


# class BooksByAuthorView(generic.ListView):
#     template_name =