from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Book,Category

# view books according to categories
class AllBooksList(ListView):
    model = Book

    context_object_name = 'book_list'
    query_set = Book.objects.all()
    template_name = 'library/allbooks.html'













