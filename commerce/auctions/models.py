from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.URLField(blank=True)

    Categories = [("1", "Category 1"), ("2", "Category 2")]

    category = models.CharField(max_length=32, choices=Categories, blank=True)

    


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    current_bid = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.user} => {self.current_bid} => {self.auction}"

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction= models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    watchlist = models.BooleanField(default=False)

    class Meta:
        unique_together = ["auction", "user"]