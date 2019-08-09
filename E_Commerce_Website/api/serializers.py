from rest_framework import serializers

from e_commerce_app.models import Category, Product, ProductHistory

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model=Product
        fields = ['id','name','description','available_quantity','seller_name','price','image','category_name']

class CategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class ProductHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductHistory
        fields = ('__all__')