from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addnewlisting", views.new_listing, name="add_new_listing"),
    path("bid", views.bid, name="bid"),
    path("close_bid", views.close_bid, name="close_bid"),
    path("watchlistfunc", views.watchlistfunc, name="watchlistfunc"),
    path("comment", views.comment, name="comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing<int:listing_id>", views.listing, name="listing")
]
