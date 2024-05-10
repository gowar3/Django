from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("random", views.rndm, name="random"),
    path("<str:entry>", views.entry, name="entry"),
    path("<str:edit>", views.edit, name="edit"),
]
