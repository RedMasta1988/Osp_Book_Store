from django.urls import path
from . import views


urlpatterns = [
    path("search/", views.search, name='q'),
    path('', views.view_home, name="home_page"),
]