from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import AuctionListingForm, BidsForm, CommentsForm
from .models import User, AuctionListing, Bids, WatchList, Comments
from django.contrib.auth.decorators import login_required
import datetime 


def index(request):
    auction_listings=AuctionListing.objects.filter(active=True)
    current_prices={}
    for listing in auction_listings:
        listing_bid=Bids.objects.filter(auction=listing).order_by('-current_bid').first()
        if listing_bid is None:
            current_price=listing.starting_bid
        else:
            current_price = listing_bid.current_bid
        current_prices[listing] = current_price

    return render(request, "auctions/index.html", {"auction_listings":auction_listings, "current_prices":current_prices})


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


@login_required()
def new_listing(request):
    if request.method=="POST":
        form = AuctionListingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            image = form.cleaned_data["image"]
            category = form.cleaned_data["category"]

            form = AuctionListing(user=request.user, title=title, description=description, starting_bid=starting_bid, image=image, category=category, auction_datetime = datetime.datetime.now())
            form.save()
            return HttpResponseRedirect(reverse("index"))
        
    return render(request, "auctions/newlistings.html", {"auction_form": AuctionListingForm()})



def listing(request, listing_id):
    try:
        listing=AuctionListing.objects.get(pk=listing_id)
    except AuctionListing.DoesNotExist:
        return render(request, "auctions/errorlisting.html")
    comments=Comments.objects.filter(auction=listing)
    

    try:
        watchlist_status = WatchList.objects.get(auction=listing_id, user = request.user).watchlist
    except (WatchList.DoesNotExist, TypeError):
        watchlist_status = False
    
    listing_bid=Bids.objects.filter(auction=listing).order_by('-current_bid').first()
    if listing_bid is None:
        current_price=listing.starting_bid
        current_price_check=listing.starting_bid
    else:
        current_price = listing_bid.current_bid
        current_price_check = float(listing_bid.current_bid) + 0.01

    return render(request, "auctions/listing.html", {"listing":listing, "current_price":current_price, "watchlist_status": watchlist_status, "bidding_form": BidsForm(min_value=current_price_check), "winner_bid": listing_bid, "comments_form":CommentsForm(), "comments":comments})


@login_required()
def bid(request):
    if request.method == "POST":
        bids_form = BidsForm (request.POST)
        if bids_form.is_valid():
            current_bid = bids_form.cleaned_data["current_bid"]
            listing_id = request.POST.get("listing_id")
            form = Bids(user=request.user, auction=AuctionListing.objects.get(pk=listing_id), current_bid=current_bid)
            form.save()
        return HttpResponseRedirect(reverse("listing", args=[listing_id]))
        

        
@login_required()
def watchlistfunc(request):
    if request.method == "POST":
        listing_id = request.POST.get("listing_id")
        listing=AuctionListing.objects.get(pk=listing_id)

        try:
            watchlistdata = WatchList.objects.get(user = request.user, auction = listing_id)
            if watchlistdata.watchlist:
                watchlistdata.watchlist=False
            else:
                watchlistdata.watchlist=True
        except WatchList.DoesNotExist:
            watchlistdata = WatchList(user=request.user, auction= listing, watchlist=True)
        watchlistdata.save()

        return HttpResponseRedirect(reverse("listing", args=[listing_id]))
        

@login_required()
def close_bid(request):
    if request.method == "POST":
        listing_id = request.POST.get("listing_id")
        listing=AuctionListing.objects.get(pk=listing_id)
        listing.active = False
        listing.save()
    
        return HttpResponseRedirect(reverse("listing", args=[listing_id]))
    

@login_required()
def comment(request):
    if request.method == "POST":
        comment_form = CommentsForm (request.POST)
        if comment_form.is_valid():
            comment = comment_form.cleaned_data["comment"]
            listing_id = request.POST.get("listing_id")
            listing=AuctionListing.objects.get(pk=listing_id)
            comment_form = Comments(user=request.user, auction=listing, comment=comment, comment_datetime = datetime.datetime.now())
            comment_form.save()

        return HttpResponseRedirect(reverse("listing", args=[listing_id]))


@login_required()
def watchlist(request):
    watchlistdata = WatchList.objects.filter(user=request.user, watchlist=True)

    return render(request, 'auctions/watchlist.html', {"watchlistdata": watchlistdata})


def categories(request):
    return render (request, 'auctions/categories.html', {"categories": AuctionListing.Categories})


def category(request, category):
    categories = AuctionListing.objects.filter(category=category, active=True)

    return render (request, 'auctions/category.html', {"categories":categories})