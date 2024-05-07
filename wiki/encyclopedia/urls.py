from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("edit", views.edit, name="edit"),
    path("<str:entry>", views.entry, name="entry")
]
