from django.urls import path
from guide import views

app_name="guide"

urlpatterns = [
    path("writer/", views.WriterList.as_view(), name="writer_list"), 
    path("writer/<int:pk>/", views.WriterDetail.as_view(), name="writer_detail"),
    path("writer/create/", views.WriterCreate.as_view(), name="writer_create"),
    path("writer/update/<int:pk>/", views.WriterUpdate.as_view(), name="writer_update"),
    path("writer/delete/<int:pk>/", views.WriterDelete.as_view(), name="writer_delete"),
    path("writer/search/<int:pk>/", views.WriterDetailFilter.as_view(), name="writer_search"),
    path("genre/", views.GenreList.as_view(), name="genre_list"), 
    path("genre/<int:pk>/", views.GenreDetail.as_view(), name="genre_detail"),
    path("genre/create/", views.GenreCreate.as_view(), name="genre_create"),
    path("genre/update/<int:pk>/", views.GenreUpdate.as_view(), name="genre_update"),
    path("genre/delete/<int:pk>/", views.GenreDelete.as_view(), name="genre_delete"),
    path("genre/search/<int:pk>/", views.GenreDetailFilter.as_view(), name="genre_search"),
    path("serie/", views.SerieList.as_view(), name="serie_list"), 
    path("serie/<int:pk>/", views.SerieDetail.as_view(), name="serie_detail"),
    path("serie/create/", views.SerieCreate.as_view(), name="serie_create"),
    path("serie/update/<int:pk>/", views.SerieUpdate.as_view(), name="serie_update"),
    path("serie/delete/<int:pk>/", views.SerieDelete.as_view(), name="serie_delete"),
    path("serie/search/<int:pk>/", views.SerieDetailFilter.as_view(), name="serie_search"),  
    path("publishing_house/", views.PublishingHouseList.as_view(), name="publishing_house_list"), 
    path("publishing_house/<int:pk>/", views.PublishingHouseDetail.as_view(), name="publishing_house_detail"),
    path("publishing_house/create/", views.PublishingHouseCreate.as_view(), name="publishing_house_create"),
    path("publishing_house/update/<int:pk>/", views.PublishingHouseUpdate.as_view(), name="publishing_house_update"),
    path("publishing_house/delete/<int:pk>/", views.PublishingHouseDelete.as_view(), name="publishing_house_delete"),
    path("publishing_house/search/<int:pk>/", views.PublishingHouseDetailFilter.as_view(), name="publishing_house_search"),

]