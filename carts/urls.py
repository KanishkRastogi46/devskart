from django.urls import path
from carts.views import *

urlpatterns = [
    path("", index, name="cart"),
    path("add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:product_id>/", remove_from_cart, name="remove_from_cart"),
    path("delete/<int:product_id>/", delete_cart_item, name="delete_cart_item"),
]
