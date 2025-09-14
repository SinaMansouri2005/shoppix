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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
    
    def calculate_avg_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count() , 1)
        return 0
    
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
    