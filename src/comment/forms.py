from django import forms
from . import models


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ("name", "comment")