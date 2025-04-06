from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

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
    context = {'products': products, 'count': products.count() if products else 0}
    return render(request, 'store/store.html', context)