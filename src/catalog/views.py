from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from . import models, forms
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class BookDetail(DetailView):
    template_name = "catalog/book_detail.html"
    model = models.Book


class BookList(ListView):
    template_name = "catalog/book_list.html"
    paginate_by = 9
    model = models.Book


class BookCreate(LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    template_name = "catalog/book_create.html"
    model = models.Book
    form_class = forms.BookModelForm
    success_url = reverse_lazy("catalog:book_list")
    login_url= "/account/login"
    permission_required = ["catalog.add_book",]
    success_message = 'Книга успешно создана!'

class BookDelete(LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, DeleteView,):
    template_name = "catalog/book_delete.html"
    model = models.Book
    success_url = reverse_lazy("catalog:book_list")
    login_url= "/account/login"
    permission_required = ["catalog.delete_book",]
    success_message = 'Книга успешно удалена!'

class BookUpdate(LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    template_name = "catalog/book_update.html"
    model = models.Book
    form_class = forms.BookModelForm
    success_url = reverse_lazy("catalog:book_list")
    login_url= "/account/login"
    permission_required = ["catalog.change_book",]
    success_message = 'Книга успешно обновлена!'

@login_required
def add_comment(request, pk):
    form = forms.CommentModelForm()
    books = get_object_or_404(models.Book, pk=pk)
    user = request.user

    if request.method == "POST":
        form = forms.CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.book = books
            comment.save()
            return redirect("catalog:book_detail", pk=books.pk)

    context = {'form': form}

    return render(request, 'catalog/comment_form.html', context)

