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

    Categories = [("Electronics", "Electronics"), 
              ("Fashion and Apparel", "Fashion and Apparel"), 
              ("Health and Beauty", "Health and Beauty"), 
              ("Home and Garden", "Home and Garden"), 
              ("Books and Media", "Books and Media"), 
              ("Sports and Outdoors", "Sports and Outdoors"), 
              ("Toys and Hobbies", "Toys and Hobbies"), 
              ("Automotive", "Automotive"), 
              ("Groceries", "Groceries"),
              ("Jewelry", "Jewelry"),
              ("Office Supplies", "Office Supplies"),
              ("Pet Supplies", "Pet Supplies"),
              ("Baby Products", "Baby Products"),
              ("Art and Craft", "Art and Craft"),
              ("Musical Instruments", "Musical Instruments"),
              ("Collectibles", "Collectibles"),
              ("Travel and Luggage", "Travel and Luggage"),
              ("Furniture", "Furniture"),
              ("Party Supplies", "Party Supplies")]

    category = models.CharField(max_length=64, choices=Categories, blank=True)

    active = models.BooleanField(default=True)

    

class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    current_bid = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user} => {self.current_bid} => {self.auction}"

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction= models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    watchlist = models.BooleanField()

    class Meta:
        unique_together = ["auction", "user"]