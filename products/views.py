# filepath: c:\Users\sinar\Desktop\project\ecommerce_shop\products\views.py
from .models import Product , Category
from django.shortcuts import render , get_object_or_404
from django.db.models import Q


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
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})



def product_search(request):
    query = request.GET.get("q" ,"")
    products = Product.objects.filter(Q(name__icontains = query)| Q(description__icontains = query)
    )if query else Product.objects.none()

    return render(request , "products/product_search.html"  , {'products':products  , 'query': query})