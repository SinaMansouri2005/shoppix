from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

Customer = get_user_model()

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ("username", "email")  


class CustomerEditform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["username" ,"email" ,"phone" ,"address" , "profile_image"]