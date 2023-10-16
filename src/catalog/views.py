from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from . import models, forms
from django.shortcuts import render

# Create your views here.


class BookDetail(DetailView):
    template_name = "catalog/book_detail.html"
    model = models.Book


class BookList(ListView):
    template_name = "book_list.html"
    paginate_by = 9
    model = models.Book


class BookCreate(CreateView):
    template_name = "catalog/book_create.html"
    model = models.Book
    form_class = forms.BookModelForm
    success_url = "/catalog/"


class BookDelete(DeleteView):
    template_name = "catalog/book_delete.html"
    model = models.Book
    success_url = "/catalog/"


class BookUpdate(UpdateView):
    template_name = "catalog/book_update.html"
    model = models.Book
    form_class = forms.BookModelForm
    success_url = "/catalog/"


def view_home(request):
    return render(request, "main.html")

