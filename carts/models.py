from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.
class Cart(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete= models.CASCADE , related_name= 'cart')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    def __str__(self):
        return f"cart of {self.customer.username}"
    
    @property
    def total_price (self):
        return sum(item.item_total for item in self.items.all())
    
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart , on_delete= models.CASCADE , related_name='items')
    product = models.ForeignKey(Product , on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default= 1)


    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"
    
    @property
    def item_total (self):
        return self.quantity * self.product.price