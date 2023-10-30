from django.urls import path
from catalog import views

app_name="catalog"

urlpatterns = [
    path("", views.BookList.as_view(), name="book_list"), 
    path("book/<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("book/create/", views.BookCreate.as_view(), name="book_create"),
    path("book/update/<int:pk>/", views.BookUpdate.as_view(), name="book_update"), 
    path("book/delete/<int:pk>/", views.BookDelete.as_view(), name="book_delete"), 
    path("book/<int:pk>/comment/", views.add_comment, name="add_comment"),
]
