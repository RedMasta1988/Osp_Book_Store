from django.contrib import admin
from . import models


# Register your models here.
class WriterAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


admin.site.register(models.Writer, WriterAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "discription")


admin.site.register(models.Genre, GenreAdmin)


class SerieAdminGenreAdmin(admin.ModelAdmin):
    list_display = ("name", "discription")


admin.site.register(models.Serie)


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ("name", "discription")


admin.site.register(models.PublishingHouse, PublishingHouseAdmin)
