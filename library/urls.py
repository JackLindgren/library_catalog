from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('authors', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:author_id>', views.books_by_author, name='authors_works'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('add_author', views.add_author, name='add_author'),
    path('add_book', views.add_book, name='add_book')
]
