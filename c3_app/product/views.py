from django.shortcuts import render, redirect
from product.forms import AddForm, SaleForm
from product.models import Product,Sale
from django.contrib.auth.decorators import login_required
from product.filters import ProductFilter

# Create your views here.
def home(request):
    products = Product.objects.all().order_by('id')
    product_filters = ProductFilter(request.GET, queryset = products)
    products = product_filters.qs

    return render(request, 'product/index.html', {
        'products': products, 'product_filters': product_filters, })

def receipt(request): 
    sales = Sale.objects.all().order_by('-id')
    return render(request, 
    'product/receipt.html', 
    {'sales': sales,})

def all_sales(request):
    product = Product.objects.all().order_by('id')
    return render(request, 'product/all_sales.html',
     {'products': product, })

def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'product/product_detail.html', {'product': product})

def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'product/receipt_detail.html', {'receipt': receipt})

def issue_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)  

    if request.method == 'POST':     
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item   
            new_sale.save()
            issued_quantity = int(request.POST['quantity'])
            if issued_item.total_quantity < issued_quantity:
                print('Not Enough Inventory')
            else:   
                issued_item.issued_quantity += issued_quantity
                issued_item.total_quantity -= issued_quantity
                issued_item.save()
            return redirect('product:home') 
    return render (request, 'product/issue_item.html',{'sales_form': sales_form, })
    
def add_to_inventory(request, pk):
    add_item = Product.objects.get(id = pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            add_item.received_quantity += added_quantity
            add_item.total_quantity += added_quantity
            add_item.save()
            return redirect('product:home')
    return render (request, 'product/add_to_inventory.html', {'form': form})