from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem , Cart , Product
from django.contrib import messages

# Create your views here.
@login_required
def cart_detail(request):
    cart , created = Cart.objects.get_or_create(customer = request.user )
    return render(request , 'cart/cart_detail.html' , {'cart': cart})



@login_required
def add_to_cart(request , product_id):
    product = get_object_or_404(Product , id = product_id)
    cart , created = Cart.objects.get_or_create(customer = request.user)
    cart_item , created = CartItem.objects.get_or_create(cart = cart , product = product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'تعداد "{product.name}" در سبد شما افزایش یافت.')
    else:
        messages.success(request, f'محصول "{product.name}" به سبد شما اضافه شد.')
    return redirect('cart:cart_detail')
@login_required
def remove_from_cart(request , cart_item_id):
    cart_item = get_object_or_404(CartItem , id = cart_item_id , cart_customer = request.user)
    cart_item.delete()
    messages.success(request, 'محصول از سبد خرید حذف شد.')
    return redirect('cart:cart_detail')
