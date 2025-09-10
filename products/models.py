from django.db import models

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