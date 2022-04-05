import django_filters
from product.models import Product, Category, Sale

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['item_name']

class CategoryFilter(django_filters.FilterSet):
    class Meta: 
        model = Category
        fields = ['name']

class SalesFilter(django_filters.FilterSet):
    class Meta: 
        model = Sale
        fields = ['car_dealership']