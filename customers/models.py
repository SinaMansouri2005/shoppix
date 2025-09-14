from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer(AbstractUser):
    phone = models.CharField(max_length=40)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='profile_imgaes/' , default= 'profile_images/default.png' , blank= True , null= True)
    
    def __str__(self):
        return self.username

