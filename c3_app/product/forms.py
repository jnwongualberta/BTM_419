from django.forms import ModelForm
from .models import *

class AddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['received_quantity']

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'car_dealership']
      

class AddInventoryForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category_name', 'item_name', 'total_quantity']

class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields =['name']

class EditSaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'car_dealership', 'item']

class EditForm(ModelForm):
    class Meta:
        model = Edit
        fields = ['text']
        
class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['text']