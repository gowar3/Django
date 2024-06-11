from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new(request):


    if request.method == "POST":

        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]

        listing = Listing.objects.create(title=title, description=description, price=price)

        return HttpResponseRedirect(reverse("index"))

    else:

        return render(request, "auctions/new.html")


def listing(request, listing):

    listing = Listing.objects.get(title = listing)

    return render(request, "auctions/listing.html", {
        "listing": listing
    })



def wishlist(request, wishlist):

    if "wishlist" not in request.session:

        request.session["wishlist"] = []



    if request.method == "POST":


        wish = Listing.objects.get(title = listing.title)

        request.session["wishlist"] += [wish]

        wishlist = request.session["wishlist"]


        return HttpResponseRedirect(reverse("wishlist", args=[wishlist]))

    return render(request, "auctions/wishlist.html", {
        "wishlist": request.session["wishlist"]
    })
