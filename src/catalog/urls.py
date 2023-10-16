from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import BookDetail, BookList, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path("", BookList.as_view()), 
    path("book/<int:pk>/", BookDetail.as_view()),
    path("book/create/", BookCreate.as_view()),
    path("book/update/<int:pk>/", BookUpdate.as_view()), 
    path("book/delete/<int:pk>/", BookDelete.as_view()), 
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
