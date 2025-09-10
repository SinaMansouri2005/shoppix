from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order

@login_required
def order_list(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail(request, pk):
    order = Order.objects.get(pk=pk, customer=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})