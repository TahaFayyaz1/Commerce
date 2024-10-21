<h1>Commerce</h1>
Project 2 for CS50’s Web Programming with Python and JavaScript.
<h2>Overview</h2>
An eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”
<h2>Specification</h2>
The project completes the following requirements:
<ul>
  <li><strong>Models: </strong>
     The application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.</li>
     <li><strong>Create Listing: </strong>
     Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).</li>
     <li><strong>Active Listings Page: </strong>
     The default route of the web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).</li>
     <li><strong>Listing Page: </strong>
     Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing.
     <ul>
       <li>If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.</li>
       <li>If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.</li>
       <li>If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.</li>
       <li>If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.</li>
       <li>Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.</li>
     </ul>
     </li>
  <li><strong>Watchlist: </strong>
     Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.</li>
   <li><strong>Categories: </strong>
     Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.</li>
  <li><strong>Django Admin Interface: </strong>
     Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.</li>
</ul>
<h2>Setup</h2>
To set up this project on your computer:

<ol>
  <li>Download this project:<br><code>gti clone https://github.com/TahaFayyaz1/CS50-Commerce.git</code></li>
  <li>Install all necessary dependencies <br><code>pip install -r requirements.txt</code></li>
  <li>Make migrations <br><code>python manage.py makemigrations</code></li>
  <li>Migrate <br><code>python manage.py migrate</code></li>
</ol>

<h2>Preview</h2>
A demonstration of my project's functionality has be recorded and uploaded on Youtube:
<a href="https://www.youtube.com/watch?v=h0llQ434Rt4&t=202s">Project Demonstration</a>
