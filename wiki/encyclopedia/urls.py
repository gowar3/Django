from django.urls import path

from . import views

app_name= "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("random", views.rndm, name="random"),
    path("<str:entry>", views.entry, name="entry"),
    path("<str:title>", views.edit, name="edit"),
]
