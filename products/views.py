# filepath: c:\Users\sinar\Desktop\project\ecommerce_shop\products\views.py
from .models import Product , Category , Review
from django.shortcuts import render , get_object_or_404 ,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.db import IntegrityError
from django.contrib import messages
from rest_framework import generics
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticatedOrReadOnly


def product_list(request , category_slug = None):
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category , slug = category_slug)
        products = Product.objects.filter(category = category)
    else:
        category = None
    return render(request, 'products/product_list.html', {'products': products , 
                                                          'categories':categories  , 
                                                          'current_category':category})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    avg_rating = product.calculate_avg_rating()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            try:
                review.save()
                messages.success(request, "Your review has been added successfully.")
            except IntegrityError:
                messages.error(request, "You have already commented on this product.")
            return redirect("product_detail", pk=product.pk)
    else:
        form = ReviewForm()

    return render(request, "products/product_detail.html", {
        "product": product,
        "reviews": reviews,
        "avg_rating": avg_rating,
        "form": form,
    })


def product_search(request):
    query = request.GET.get("q" ,"")
    products = Product.objects.filter(Q(name__icontains = query)| Q(description__icontains = query)
    )if query else Product.objects.none()

    return render(request , "products/product_search.html"  , {'products':products  , 'query': query})





def home_products(request):
    discounted_items = Product.objects.filter(discount_price__isnull = False).order_by("id")[:10]
    top_selling_items = Product.objects.order_by("-sold_count")[:10]
    return render(request , "shop/home/html" , {"discounted_items":discounted_items , "top_selling_items":top_selling_items})



def discounted_products_list(request):
    products = Product.objects.filter(discount_price__isnull=False)
    return render(request, "shop/product_list.html", {"products": products, "title": "محصولات تخفیف‌دار"})

def best_selling_products_list(request):
    products = Product.objects.order_by("-sold_count")
    return render(request, "shop/product_list.html", {"products": products, "title": "محصولات پرفروش"})
