from django.shortcuts import render
from rest_framework import generics
from e_commerce_app.models import Product, Category, ProductHistory
from .serializers import ProductSerializer, CategoriSerializer, ProductHistorySerializer

# Create your views here.
class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriSerializer

class HistoryAPIView(generics.ListAPIView):
    queryset = ProductHistory.objects.all()
    serializer_class = ProductHistorySerializer