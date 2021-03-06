from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('authors', views.AuthorListView.as_view(), name='authors'),
    path('languages', views.LanguageListView.as_view(), name='languages'),
    path('languages/<int:language_id>', views.books_by_language, name='language_books'),
    path('authors/<int:author_id>', views.books_by_author, name='authors_works'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('add_author', views.add_author, name='add_author'),
    path('add_book', views.add_book, name='add_book'),
    path('upload_authors', views.upload_authors, name='upload_authors'),
    path('upload_books', views.upload_books, name='upload_books')
]
