from django import forms
from .models import User, AuctionListing, Bids, Comments, WatchList
from django.core.validators import MinValueValidator


class AuctionListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = "__all__"


class BidsForm(forms.ModelForm):
    current_bid = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    class Meta:
        model= Bids
        fields = ['current_bid']

    def __init__(self, *args, min_value=None, **kwargs):
        super().__init__(*args, **kwargs)
        current_bid = self.fields['current_bid']
        current_bid.min_value = min_value
        if min_value is not None:
            current_bid.validators.append(MinValueValidator(min_value))
            current_bid.widget.attrs['min'] = min_value

