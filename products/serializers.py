from rest_framework import serializers
from .models import Product , Review


class ProductSerializer(serializers.ModelSerializer):
    avg_rating  =  serializers.FloatField(read_only = True)

    class Meta:
        model  = Product
        fields = ['id'  , 'name' , 'description' , 'price' , 'stock'  , 'avg_rating' ]


class ReviewSerializer(serializers.ModelSerializer):
    user  = serializers.StringRelatedField(read_only = True)

    class Meta :
        model = Review
        fields  = ['id' , 'user' , 'rating'  , 'comment' , 'created_at']