from django.db import models
from customers.models import Customer

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length= 220 , unique= True , blank= True  )

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length= 220 , unique= True , blank= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dscount_price = models.DecimalField(max_digits= 10 ,decimal_places= 2 , null=True  , blank= True)
    sold_count = models.PositiveIntegerField(default= 0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    image = models.ImageField(blank= True , null= True)

    def __str__(self):
        return self.name
    
    def calculate_avg_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count() , 1)
        return 0
    
    def has_discount(self):
        return self.dicount_price is not None and  self.discount_price < self.price
    
    def final_price(self):
        if self.discount_price and self.discount_price < self.price:
            return self.discount_price
        return self.price
    
class Review (models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete= models.CASCADE , related_name = 'reviews')
    rating = models.PositiveIntegerField(default= 1)
    comment  = models.TextField(blank= True)
    created_at = models.DateTimeField (auto_now_add= True)
    class Meta():
        unique_together = ("product" , 'customer')

    def __str__(self):
        return f"{self.customer.username} - {self.product.name} ({self.rating})"
    