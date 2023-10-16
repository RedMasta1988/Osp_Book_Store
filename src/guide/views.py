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


class WriterCreate(CreateView):
    template_name = "guide/writer/writer_create.html"
    model = models.Writer
    form_class = forms.WriterModelForm
    success_url = "/guide/writer/"


class WriterDelete(DeleteView):
    template_name = "guide/writer/writer_delete.html"
    model = models.Writer
    success_url = "/guide/writer/"


class WriterUpdate(UpdateView):
    template_name = "guide/writer/writer_update.html"
    model = models.Writer
    form_class = forms.WriterModelForm
    success_url = "/guide/writer/"


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


class GenreCreate(CreateView):
    template_name = "guide/genre/genre_create.html"
    model = models.Genre
    form_class = forms.GenreModelForm
    success_url = "/guide/genre/"


class GenreDelete(DeleteView):
    template_name = "guide/genre/genre_delete.html"
    model = models.Genre
    success_url = "/guide/genre/"


class GenreUpdate(UpdateView):
    template_name = "guide/genre/genre_update.html"
    model = models.Genre
    form_class = forms.GenreModelForm
    success_url = "/guide/genre/"


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


class SerieCreate(CreateView):
    template_name = "guide/serie/serie_create.html"
    model = models.Serie
    form_class = forms.SerieModelForm
    success_url = "/guide/serie/"


class SerieDelete(DeleteView):
    template_name = "guide/serie/serie_delete.html"
    model = models.Serie
    success_url = "/guide/serie/"


class SerieUpdate(UpdateView):
    template_name = "guide/serie/serie_update.html"
    model = models.Serie
    form_class = forms.SerieModelForm
    success_url = "/guide/serie/"


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


class PublishingHouseCreate(CreateView):
    template_name = "guide/publishing_house/publishing_house_create.html"
    model = models.PublishingHouse
    form_class = forms.PublishingHouseModelForm
    success_url = "/guide/publishing_house/"


class PublishingHouseDelete(DeleteView):
    template_name = "guide/publishing_house/publishing_house_delete.html"
    model = models.PublishingHouse
    success_url = "/guide/publishing_house/"


class PublishingHouseUpdate(UpdateView):
    template_name = "guide/publishing_house/publishing_house_update.html"
    model = models.PublishingHouse
    form_class = forms.PublishingHouseModelForm
    success_url = "/guide/publishing_house/"
