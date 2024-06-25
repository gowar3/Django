from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Comment, Bid
from .serializers import ListingSerializer  # Assuming your serializer is in a file named serializers.py


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

        creator = request.user.username
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]

        listing = Listing.objects.create(creator=creator, title=title, description=description, price=price)

        return HttpResponseRedirect(reverse("index"))

    else:

        return render(request, "auctions/new.html")


def listing(request, listing):

    if "comments" not in request.session:

        request.session["comments"] = ()

    if "bids" not in request.session:

        request.session["bids"] = ()

    error = ""
    listing = Listing.objects.get(title = listing)
    username = request.user.username

    if request.method == "POST":

        ##username = request.POST["username"]

        comment = request.POST.get("comment", "")

        bid = request.POST.get("bid", "")


        if comment != "":


            new_comment = Comment.objects.create(poster=username, comment=comment, listing=listing)

            new_comment.listings.add(listing)


        if bid != "" and int(bid) > listing.price:


            new_bid = Bid.objects.create(owner=username, offer=bid, listing=listing)

            new_bid.bids.add(listing)

        else:

            error = "Invalid bid. Must be higher than the cost"

    return render(request, "auctions/listing.html", {
        "error": error,
        "listing": listing,
        "comments": listing.comments.all(),
        "bids": listing.bids.all()
    })





def wishlist(request, user):

#    if "wishlist" not in request.session:

 #       request.session["wishlist"] = []

    wisher = User.objects.get(username = user)


    if request.method == "POST":

        listing_title = request.POST["listing_title"]

        wish = Listing.objects.get(title = listing_title)

        wish.users.add(wisher)

     #   serializer = ListingSerializer(wish)

      #  serialized_data = serializer.data

       # request.session["wishlist"] += [serialized_data]


       # return HttpResponseRedirect(reverse("wishlist", args=[user]))


    return render(request, "auctions/wishlist.html", {
        "wishlist": wisher.wishlist.all()
    })


##implement the filter to allow bids higher than the cost
