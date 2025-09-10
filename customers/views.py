from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .forms import CustomerCreationForm
from .models import Customer


class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'customers/customer_list.html', {'customers': customers})


class CustomerDetailView(View):
    def get(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        return render(request, 'customers/customer_detail.html', {'customer': customer})


def register(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerCreationForm()
    return render(request, 'customers/register.html', {'form': form})
