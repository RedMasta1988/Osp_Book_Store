from django import forms
from . import models


class WriterModelForm(forms.ModelForm):
    class Meta:
        model = models.Writer
        fields = ("name", "discription")


class GenreModelForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ("name", "discription")


class SerieModelForm(forms.ModelForm):
    class Meta:
        model = models.Serie
        fields = ("name", "discription")


class PublishingHouseModelForm(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = ("name", "discription")
