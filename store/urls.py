from django.urls import path
from store.views import *

urlpatterns = [
    path("", index, name="store"),
    path("<slug:category_name>/", index, name="product_by_category"),
    path("<slug:category_name>/<slug:product_name>/", product_page, name="product_page_with_category"),
    path("<slug:product_name>/", product_page, name="product_page")
]
