from django import forms
from .models import AuctionListing, Bids, Comments
from django.core.validators import MinValueValidator


class AuctionListingForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}), label="")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}), label="")
    starting_bid = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Starting Bid"}), max_digits=12, decimal_places=2, label= "")
    image = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL for an Image'}), label="")
    category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}), choices=AuctionListing.Categories, label="")
    class Meta:
        model = AuctionListing
        exclude = ['user', 'active']
        


class BidsForm(forms.ModelForm):
    current_bid = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Bid"}), max_digits=12, decimal_places=2, required=False, label= "")
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


class CommentsForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Add a comment...'}), label="")
    class Meta:
        model = Comments
        fields = ['comment']