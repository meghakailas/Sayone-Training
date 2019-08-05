from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from .forms import AddBookForm
from library.models import Book
from django.views.generic.edit import DeleteView

def addbooks_view(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else :
            print(form.errors)
        return render(request,'register/adminpage.html')


    else:

        form = AddBookForm()
        return render(request,'register/addbooks.html',{'form': form } )



def deletebooks_view(request):
    book_list = Book.objects.all()
    context = {'books': book_list}
    return render(request,'register/deletebooks.html',context)

class DeleteBooksView(DeleteView):
    model = Book
    success_url = reverse_lazy('admapp:deletebooks')
    template_name = "register/confirmdelete.html"

class AdminBooksList(ListView):
    model = Book

    context_object_name = 'book_list'
    query_set = Book.objects.all()
    paginate_by = 2
    template_name = 'library/allbookadmin.html'
