from django.shortcuts import render, redirect
from carts.models import Cart, CartItems
from store.models import Product

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def index(request, total_price=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItems.objects.filter(cart=cart, is_active=True).all()
        for cart_item in cart_items:
            total_price += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity 
        tax = total_price * 0.04
        grand_total = total_price + tax
    except Cart.DoesNotExist:
        pass
    context = {
        "cart_items": cart_items, 
        "total_price": total_price,
        "tax": tax,
        "grand_total": grand_total, 
        "quantity": quantity
    }
    return render(request, "store/cart.html", context=context)


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()
    
    try:
        cart_item = CartItems.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart')
    

def remove_from_cart(request, product_id=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItems.objects.filter(cart=cart, product=product_id).first()
        cart_item.quantity -= 1
        if cart_item.quantity <= 0:
            cart_item.delete()
        else:
            cart_item.save()
    except CartItems.DoesNotExist:
        pass
    return redirect('cart')


def delete_cart_item(request, product_id=None):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItems.objects.filter(cart=cart, product=product_id).first()
    if cart_item:
        cart_item.delete()
    return redirect('cart')