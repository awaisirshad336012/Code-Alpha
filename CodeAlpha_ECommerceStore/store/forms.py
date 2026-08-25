from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "address", "city", "phone"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Full name"}),
            "address": forms.TextInput(attrs={"placeholder": "Street address"}),
            "city": forms.TextInput(attrs={"placeholder": "City"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone number"}),
        }
