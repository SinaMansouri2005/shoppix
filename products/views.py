# filepath: c:\Users\sinar\Desktop\project\ecommerce_shop\products\views.py
from .models import Product , Category , Review
from django.shortcuts import render , get_object_or_404 ,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm


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
    reviews  =  product.reviews.all()
    avg_rating = product.calculate_avg_rating()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit= False)
            review.product = product
            review.customer = request.user
            review.save()
            return redirect("product_detail" , pk = product.id)
        
    else:
        form = ReviewForm()

    return render(request, 'products/product_detail.html', {'product': product , 'reviews':reviews ,'avg_rating':avg_rating ,'form':form})



def product_search(request):
    query = request.GET.get("q" ,"")
    products = Product.objects.filter(Q(name__icontains = query)| Q(description__icontains = query)
    )if query else Product.objects.none()

    return render(request , "products/product_search.html"  , {'products':products  , 'query': query})

@login_required
def add_review(request , product_id):
    product = get_object_or_404(Product  , product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit= False)
            review.product = product
            review.customer = request.user
            review.save()
            return redirect("product_detail" , pk = product.id)
        
    else:
        form = ReviewForm()
    return render(request , "products/add_review.html" , {"form":form , "product":product})
