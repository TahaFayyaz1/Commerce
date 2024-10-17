from django import forms
from .models import User, AuctionListing, Bids, Comments, WatchList


class AuctionListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = "__all__"

class WatchListForm(forms.ModelForm):
    watchlist = forms.BooleanField(required=False)
    class Meta:
        model = WatchList
        fields = ['watchlist']