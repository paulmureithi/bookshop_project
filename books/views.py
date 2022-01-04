from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Book


# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'


# adding a book
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = [
        'title',
        'author',
        'price',
        'description',
        'cover',
    ]
    template_name = 'books/add_book.html'