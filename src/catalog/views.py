from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from . import models, forms
from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone


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


def search(request):

    query = request.GET.get('q')
    
    if query=='':
        return render(request, "main.html") 
    
    object_list = models.Book.objects.filter(
            Q(title_of_the_book__icontains=query))
        
    if object_list.count()>=1:
        context={'object_list': object_list}
        return render(request, 'catalog/book_list.html', context)
        
    object_list = models.Genre.objects.filter(
                Q(name__icontains=query))
        
    if object_list.count()>=1:
        context={'object_list': object_list}
        return render(request, 'guide/genre/genre_list.html', context)
        

    object_list = models.Serie.objects.filter(
            Q(name__icontains=query))

    if object_list.count()>=1:
        context={'object_list': object_list}
        return render(request, 'guide/serie/serie_list.html', context)
        
    object_list = models.Writer.objects.filter(
            Q(name__icontains=query))
        
    if object_list.count()>=1:
        context={'object_list': object_list}
        return render(request, 'guide/writer/writer_list.html', context)
        

    object_list = models.PublishingHouse.objects.filter(
            Q(name__icontains=query))
        
    if object_list.count()>=1:
        context={'object_list': object_list}
        return render(request, 'guide/publishing_house/publishing_house_list.html', context)

    else:
        return render(request, "main.html")

def view_home(request):
    object_list = models.Book.objects.all()
    zz_list=models.Book.objects.all().filter(created__lt=timezone.now())
    context={'object_list': object_list, "zz_list": zz_list}
    return render(request, "main.html", context)

