from django.urls import path
from store.views import *

urlpatterns = [
    path("", index, name="index"),
    path("<slug:category_name>/", index, name="product_by_category"),
]
