from django.contrib import admin
from .models import Category, Product, ProductHistory,OtherForm


# Register your models here.
class ProductModel(admin.ModelAdmin):
    list_display = ["__str__"]
    list_per_page = 10


class CategoryModel(admin.ModelAdmin):
    list_display = ["__str__"]

class OtherFormModel(admin.ModelAdmin):
    list_display = ["__str__"]


class ProductHistoryModel(admin.ModelAdmin):
    list_display = ["__str__"]


admin.site.register(Product, ProductModel)
admin.site.register(Category, CategoryModel)
admin.site.register(OtherForm, OtherFormModel)
admin.site.register(ProductHistory, ProductHistoryModel)


