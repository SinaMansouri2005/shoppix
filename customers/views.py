from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required 
from .forms import CustomerCreationForm , CustomerEditform
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


@login_required
def profile_detail(request):
    return render(request , 'customers/profile_detail.html' , {'user':request.user})


@login_required 
def profile_edit(request):
    if request.method == 'POST':
        form  = CustomerEditform(request.POST ,request.FILES, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('customers:profile')
    else:
            form = CustomerEditform(instance= request.user)
    return render(request , 'customers/edit_profile.html' , {"form": form})