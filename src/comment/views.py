from django.shortcuts import render
from django.views.generic import CreateView
from . import models, forms
# Create your views here.
class CommentCreate(CreateView):
    template_name="comment.html"
    model = models.Comment
    form_class = forms.CommentModelForm
    success_url = "/"

