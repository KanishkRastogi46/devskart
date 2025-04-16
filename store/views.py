from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
from store.models import Product
from carts.models import Cart, CartItems
from carts.views import _cart_id

# Create your views here.
def index(request, category_name=None):
    category = None
    products = None
    if category_name:
        try:
            category = get_object_or_404(Category, slug=category_name)
            products = Product.objects.filter(category=category).filter(is_available=True) if category else None
        except Exception:
            pass
    else:     
        products = Product.objects.all().filter(is_available=True)
    context = {'products': products, 'category': category_name, 'count': products.count() if products else 0}
    return render(request, 'store/store.html', context)


def product_page(request, category_name=None, product_name=None):
    product = get_object_or_404(Product, slug=product_name, category__slug=category_name) if category_name else get_object_or_404(Product, slug=product_name)
    try:
        in_cart = CartItems.objects.filter(CartItems, product=product, cart__cart_id=_cart_id(request)).exists()
    except Exception:
        in_cart = None
    return render(request, 'store/product_page.html', {'product': product, 'in_cart': in_cart})