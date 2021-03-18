from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="Track"),
    path("search/", views.search, name="Search"),
    path("productview/<int:myid>", views.productview, name="Product"),
    path("checkout/", views.check, name="CheckOut"),
    ]