from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=False, primary_key=True)
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.cart_id}"
    
    
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    # def add_to_cart(self):
    #     return reverse('add_to_cart', args=[self.product])
    
    def __str__(self):
        return f"{self.product.product_name} in {self.cart.cart_id}"