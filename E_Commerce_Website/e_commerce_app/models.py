from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        unique_together = (('name'),)

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField()
    available_quantity = models.PositiveIntegerField(default=0)
    seller_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class OtherForm(models.Model):
    type = (
        ('BUYER', 'BUYER'),
        ('SELLER', 'SELLER')
    )
    name = models.CharField(max_length=100, editable=False)
    mobile_no = models.CharField(max_length=11)
    account_type = models.CharField(max_length=8, choices=type)

class ProductHistory(models.Model):
    email = models.EmailField(max_length=100, editable=False)
    product_name = models.CharField(max_length=100, editable=False)
    unit_price = models.PositiveIntegerField(default=0, editable=False)
    select_quantity = models.PositiveIntegerField(default=0, editable=False)
    total_price = models.PositiveIntegerField(default=0, editable=False)
