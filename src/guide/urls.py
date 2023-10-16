from django.urls import path
from guide import views


urlpatterns = [
    path("serie/search/<int:pk>/", views.SerieDetailFilter.as_view()),
    path("writer/", views.WriterList.as_view()), 
    path("writer/<int:pk>/", views.WriterDetail.as_view()),
    path("writer/create/", views.WriterCreate.as_view()),
    path("writer/update/<int:pk>/", views.WriterUpdate.as_view()),
    path("writer/delete/<int:pk>/", views.WriterDelete.as_view()),
    path("writer/search/<int:pk>/", views.WriterDetailFilter.as_view()),
    path("genre/", views.GenreList.as_view()), 
    path("genre/<int:pk>/", views.GenreDetail.as_view()),
    path("genre/create/", views.GenreCreate.as_view()),
    path("genre/update/<int:pk>/", views.GenreUpdate.as_view()),
    path("genre/delete/<int:pk>/", views.GenreDelete.as_view()),
    path("genre/search/<int:pk>/", views.GenreDetailFilter.as_view()),
    path("serie/", views.SerieList.as_view()), 
    path("serie/<int:pk>/", views.SerieDetail.as_view()),
    path("serie/create/", views.SerieCreate.as_view()),
    path("serie/update/<int:pk>/", views.SerieUpdate.as_view()),
    path("serie/delete/<int:pk>/", views.SerieDelete.as_view()),
    path("serie/search/<int:pk>/", views.SerieDetailFilter.as_view()),
    path("publishing_house/", views.PublishingHouseList.as_view()), 
    path("publishing_house/<int:pk>/", views.PublishingHouseDetail.as_view()),
    path("publishing_house/create/", views.PublishingHouseCreate.as_view()),
    path("publishing_house/update/<int:pk>/", views.PublishingHouseUpdate.as_view()),
    path("publishing_house/delete/<int:pk>/", views.PublishingHouseDelete.as_view()),
    path("publishing_house/search/<int:pk>/", views.PublishingHouseDetailFilter.as_view()),

]