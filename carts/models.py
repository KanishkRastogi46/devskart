from django.db import models
from accounts.models import CustomUser
from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=False, primary_key=True)
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    num_of_items = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Cart of {self.user.username}"
    
    
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.product.product_name} in {self.cart.user.username}'s cart"