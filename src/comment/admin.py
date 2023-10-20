from django.contrib import admin
from . import models


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name","comment","publish")
    ordering = ("name",)
admin.site.register(models.Comment, CommentAdmin)