from django.contrib import admin
from . import models
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title_of_the_book', 'active', 'publish', 'rating', 'price')
    list_filter = ('title_of_the_book', 'writer', 'genre', 'active', 'publish', 'rating', 'publishing_house')
    search_fields = ('title_of_the_book', 'writer', 'genre')
    ordering = ['title_of_the_book', 'publish', 'rating']
admin.site.register(models.Book, BookAdmin)
