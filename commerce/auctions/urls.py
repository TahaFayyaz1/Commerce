from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addnewlisting", views.new_listing, name="add_new_listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing<int:listing_id>", views.listing, name="listing")
]
