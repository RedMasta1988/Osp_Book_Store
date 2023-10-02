from django.contrib import admin
from . import models
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title_of_the_book', 'active', 'publish', 'rating', 'publishing_house')
    list_filter = ('title_of_the_book', 'writer', 'genre', 'active', 'publish', 'rating', 'publishing_house')
    search_fields = ('title_of_the_book', 'writer', 'genre')
    ordering = ['title_of_the_book', 'publish', 'rating']
admin.site.register(models.Book, BookAdmin)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic')
    list_filter = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')
    ordering = ['last_name']
admin.site.register(models.Writer, WriterAdmin)
admin.site.register(models.Serie)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'discription')
admin.site.register(models.Genre, GenreAdmin)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'discription')
admin.site.register(models.PublishingHouse,PublishingHouseAdmin)