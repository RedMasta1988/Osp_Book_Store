from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from comment.models import Comment
from catalog import models


# Create your views here.
def search(request):
    query = request.GET.get("q")

    if query == "":
        return render(request, "home/search.html")

    object_list = models.Book.objects.filter(Q(title_of_the_book__icontains=query))

    if object_list.count() >= 1:
        context = {"object_list": object_list}
        return render(request, "catalog/book_list.html", context)

    object_list = models.Genre.objects.filter(Q(name__icontains=query))

    if object_list.count() >= 1:
        context = {"object_list": object_list}
        return render(request, "guide/genre/genre_list.html", context)

    object_list = models.Serie.objects.filter(Q(name__icontains=query))

    if object_list.count() >= 1:
        context = {"object_list": object_list}
        return render(request, "guide/serie/serie_list.html", context)

    object_list = models.Writer.objects.filter(Q(name__icontains=query))

    if object_list.count() >= 1:
        context = {"object_list": object_list}
        return render(request, "guide/writer/writer_list.html", context)

    object_list = models.PublishingHouse.objects.filter(Q(name__icontains=query))

    if object_list.count() >= 1:
        context = {"object_list": object_list}
        return render(
            request, "guide/publishing_house/publishing_house_list.html", context
        )

    else:
        return render(request, "home/search.html")


def view_home(request):
    rating_list = models.Book.objects.all().filter(rating=10)[:5]
    last_list = (
        models.Book.objects.all()
        .filter(publish__lte=timezone.now())
        .order_by("-publish")[:5]
    )
    new_list = models.Book.objects.all().filter(year_of_publication=2023)[:5]
    comment_list = (
        Comment.objects.all()
        .filter(publish__lte=timezone.now())
        .order_by("-publish")[:4]
    )
    context = {
        "rating_list": rating_list,
        "last_list": last_list,
        "new_list": new_list,
        "comment_list": comment_list,
    }

    return render(request, "home/main.html", context)
