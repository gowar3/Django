from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("<str:listing>", views.listing, name="listing"),
    path("<str:user>/wishlist", views.wishlist, name="wishlist"),
    path("category/<str:category>", views.category, name="category")
]
