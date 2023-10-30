from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


class WriterDetail(DetailView):
    template_name = "guide/writer/writer_detail.html"
    model = models.Writer


class WriterDetailFilter(DetailView):
    template_name = "catalog/book_list_filter.html"
    model = models.Writer


class WriterList(ListView):
    template_name = "guide/writer/writer_list.html"
    paginate_by = 9
    model = models.Writer


class WriterCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "guide/writer/writer_create.html"
    model = models.Writer
    form_class = forms.WriterModelForm
    success_url = reverse_lazy("guide:writer_list")
    login_url = "/account/login"
    permission_required = "guide.add_writer"


class WriterDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = "guide/writer/writer_delete.html"
    model = models.Writer
    success_url = reverse_lazy("guide:writer_list")
    login_url = "/account/login"
    permission_required = "guide.delete_writer"


class WriterUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "guide/writer/writer_update.html"
    model = models.Writer
    form_class = forms.WriterModelForm
    success_url = reverse_lazy("guide:writer_list")
    login_url = "/account/login"
    permission_required = "guide.change_writer"


class GenreDetail(DetailView):
    template_name = "guide/genre/genre_detail.html"
    model = models.Genre


class GenreDetailFilter(DetailView):
    template_name = "catalog/book_list_filter.html"
    model = models.Genre


class GenreList(ListView):
    template_name = "guide/genre/genre_list.html"
    paginate_by = 9
    model = models.Genre


class GenreCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "guide/genre/genre_create.html"
    model = models.Genre
    form_class = forms.GenreModelForm
    success_url = reverse_lazy("guide:genre_list")
    login_url = "/account/login"
    permission_required = "guide.add_genre"


class GenreDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = "guide/genre/genre_delete.html"
    model = models.Genre
    success_url = reverse_lazy("guide:genre_list")
    login_url = "/account/login"
    permission_required = "guide.delete_genre"


class GenreUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "guide/genre/genre_update.html"
    model = models.Genre
    form_class = forms.GenreModelForm
    success_url = reverse_lazy("guide:genre_list")
    login_url = "/account/login"
    permission_required = "guide.change_genre"


class SerieDetail(DetailView):
    template_name = "guide/serie/serie_detail.html"
    model = models.Serie


class SerieDetailFilter(DetailView):
    template_name = "catalog/book_list_filter.html"
    model = models.Serie


class SerieList(ListView):
    template_name = "guide/serie/serie_list.html"
    paginate_by = 9
    model = models.Serie


class SerieCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "guide/serie/serie_create.html"
    model = models.Serie
    form_class = forms.SerieModelForm
    success_url = reverse_lazy("guide:serie_list")
    login_url = "/account/login"
    permission_required = "guide.add_genre"


class SerieDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = "guide/serie/serie_delete.html"
    model = models.Serie
    success_url = reverse_lazy("guide:genre_list")
    login_url = "/account/login"
    permission_required = "guide.delete_genre"


class SerieUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "guide/serie/serie_update.html"
    model = models.Serie
    form_class = forms.SerieModelForm
    success_url = reverse_lazy("guide:genre_list")
    login_url = "/account/login"
    permission_required = "guide.change_genre"


class PublishingHouseDetail(DetailView):
    template_name = "guide/publishing_house/publishing_house_detail.html"
    model = models.PublishingHouse


class PublishingHouseDetailFilter(DetailView):
    template_name = "catalog/book_list_filter.html"
    model = models.PublishingHouse


class PublishingHouseList(ListView):
    template_name = "guide/publishing_house/publishing_house_list.html"
    paginate_by = 9
    model = models.PublishingHouse


class PublishingHouseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "guide/publishing_house/publishing_house_create.html"
    model = models.PublishingHouse
    form_class = forms.PublishingHouseModelForm
    success_url = reverse_lazy("guide:publishing_house_list")
    login_url = "/account/login"
    permission_required = "guide.add_genre"


class PublishingHouseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = "guide/publishing_house/publishing_house_delete.html"
    model = models.PublishingHouse
    success_url = reverse_lazy("guide:publishing_house_list")
    login_url = "/account/login"
    permission_required = "guide.delete_genre"


class PublishingHouseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "guide/publishing_house/publishing_house_update.html"
    model = models.PublishingHouse
    form_class = forms.PublishingHouseModelForm
    success_url = reverse_lazy("guide:publishing_house_list")
    login_url = "/account/login"
    permission_required = "guide.change_genre"
