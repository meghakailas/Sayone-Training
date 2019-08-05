from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Book,Category
from django.db.models import Q


# view books according to categories
class AllBooksList(ListView):
    model = Book

    context_object_name = 'book_list'
    query_set = Book.objects.all()
    paginate_by = 2
    template_name = 'library/allbooks.html'

def download_view(request,book_id):
    sel_book = get_object_or_404(Book,pk=book_id)
    context = {
        'book': sel_book

    }
    return render(request,'library/download.html',context)

def catrom_view(request):

    sel_books = Book.objects.filter(category__cname__icontains='Romance')
    context = {
        'books': sel_books
    }
    return render(request,'library/categorywise.html',context)

def catdrama_view(request):
    sel_book = Book.objects.filter(category__cname__icontains='drama')
    context = {
        'books': sel_book
    }
    return render(request, 'library/categorywise.html', context)

def catcrime_view(request):
    sel_book = Book.objects.filter(category__cname__icontains='crime')
    context = {
        'books': sel_book
    }
    return render(request, 'library/categorywise.html', context)

def catdet_view(request):
    sel_book = Book.objects.filter(category__cname__icontains='detective')
    context = {
        'books': sel_book
    }
    return render(request, 'library/categorywise.html', context)

def catfan_view(request):
    sel_book = Book.objects.filter(category__cname__icontains='fantasy')
    context = {
        'books': sel_book
    }
    return render(request, 'library/categorywise.html', context)











