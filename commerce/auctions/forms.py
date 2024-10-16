from django import forms
from .models import User, AuctionListing, Bids, Comments


class AuctionListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = "__all__"