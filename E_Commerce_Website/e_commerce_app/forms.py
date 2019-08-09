from django import forms
from django.contrib.auth.models import User
from . models import Product, Category, OtherForm
class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',
                  'description',
                  'available_quantity',
                  'seller_name',
                  'price',
                  'image',
                  'category'
                  ]
class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}))
    email = forms.CharField(max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password','confirm_password']

class NewForm(forms.ModelForm):
    class Meta:
        model = OtherForm
        fields = ['mobile_no','account_type']