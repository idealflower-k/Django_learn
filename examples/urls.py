from django.urls import path, include
from .views import BooksAPI, BookAPI, BooksAPIMixins, BookAPIMixins

urlpatterns = [
	path("books/", BooksAPI.as_view()),
	path("book/<int:bid>/", BookAPI.as_view()),
	path("mixin/books/", BooksAPIMixins.as_view()),
	path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
]
