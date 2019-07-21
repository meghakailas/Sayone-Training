from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from library.models import Book


def searchView(request):

    query = request.GET.get('q')
    if query :
        results = Book.objects.filter(Q(bname__icontains=query)|Q(author__icontains=query)|Q(publisher__icontains=query))

        if results:

            return render(request,'search/query.html',{'results':results})
        else:
            messages.error(request,"no results found")
            return redirect('/')

    else :
        messages.error(request,"enter something")
        return redirect('/')