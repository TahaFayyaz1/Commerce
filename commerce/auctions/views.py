from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import AuctionListingForm, BidsForm
from .models import User, AuctionListing, Bids, WatchList
import sys


def index(request):
    auction_listings=AuctionListing.objects.all()
    return render(request, "auctions/index.html", {"auction_listings":auction_listings})


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



def new_listing(request):
    if request.method=="POST":
        form = AuctionListingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        
    return render(request, "auctions/newlistings.html", {"auction_form": AuctionListingForm()})



def listing(request, listing_id):
    listing=AuctionListing.objects.get(pk=listing_id)
    
    try:
        watchlist_status = WatchList.objects.get(auction=listing_id, user = request.user).watchlist
    except WatchList.DoesNotExist:
        watchlist_status = False
    
    try:
        listing_bid=Bids.objects.filter(auction=listing).order_by('-current_bid').first()
        current_price = listing_bid.current_bid

    except Bids.DoesNotExist:
        current_price=listing.starting_bid

    return render(request, "auctions/listing.html", {"listing":listing, "current_price":current_price, "watchlist_status": watchlist_status, "bidding_form": BidsForm(min_value=current_price)})


def bid(request):
    if request.method == "POST":
        bids_form = BidsForm (request.POST)
        if bids_form.is_valid():
            current_bid = bids_form.cleaned_data["current_bid"]
            listing_id = request.POST.get("listing_id")
            form = Bids(user=request.user, auction=AuctionListing.objects.get(pk=listing_id), current_bid=current_bid)
            form.save()
            return HttpResponseRedirect(reverse("listing", args=[listing_id]))
        
        else:
            return HttpResponse("hello")
        

def watchlistfunc(request):
    if request.method == "POST":
        listing_id = request.POST.get("listing_id")
        listing = request.POST.get("listing")
        try:
            print("hereee")
            watchlistdata = WatchList.objects.get(user = request.user, auction = listing_id)
            if watchlistdata.watchlist:
                watchlistdata.watchlist=False
            else:
                watchlistdata.watchlist=True
        except WatchList.DoesNotExist:
            watchlistdata = WatchList(user=request.user, auction= eval(listing), watchlist=False)
        watchlistdata.save()

        return HttpResponseRedirect(reverse("listing", args=[listing_id]))
        

def close_bid(request):
    pass
