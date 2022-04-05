from django.shortcuts import render, redirect
from product.forms import AddForm, SaleForm, AddInventoryForm,AddCategoryForm, EditSaleForm, EditForm, EntryForm
from product.models import Product,Sale
from django.contrib.auth.decorators import login_required
from product.filters import ProductFilter
from io import BytesIO
import matplotlib.pyplot as plt
import base64

# Create your views here.

#inventory page
def inventory(request):
    products = Product.objects.all().order_by('id')
    product_filters = ProductFilter(request.GET, queryset = products)
    products = product_filters.qs
    return render(request, 'product/index.html', {
        'products': products, 'product_filters': product_filters, })

def home(request):
    return render(request, 'product/landing_page.html')

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
            return redirect('product:inventory') 
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
            return redirect('product:inventory')
    return render (request, 'product/add_to_inventory.html', {'form': form})

def add_new_inventory(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = AddInventoryForm()
    else:
        # POST data submitted; process data.
        form = AddInventoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:inventory')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'product/add_new_inventory.html', context)

def edit_inventory(request, pk):
    """Edit an existing entry."""
    edit_item = Product.objects.get(id = pk)   
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = AddInventoryForm(instance=edit_item)
    else:
        # POST data submitted; process data.
        form = AddInventoryForm(instance=edit_item, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:inventory')    
    context = { 'form': form}
    return render(request, 'product/edit_inventory.html', context)

def add_category(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = AddCategoryForm()
    else:
        # POST data submitted; process data.
        form = AddCategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:inventory')
    context = {'form': form}
    return render(request, 'product/add_category.html', context)

def plot(request):
    labels = ['Window Tint', 'Undercoating', 'Car Alarm', 'Film_3M', 'Rustproofing']
    units_of = [10, 35, 30, 35, 5]
    width = 0.40      
    fig, ax = plt.subplots()

    # Optional: chart title and label axes.
 
    ax.bar(labels, units_of, width, color = ('y','g', 'g','g','r'))
    ax.set_ylabel('Number of units')
    ax.set_title('Inventory Levels ')

    # Create a bytes buffer for saving image
    figbuffer = BytesIO()
    plt.savefig(figbuffer, format='png', dpi=350)
    image_base640=base64.b64encode(figbuffer.getvalue())
    image_base64 = image_base640.decode('utf-8')
    figbuffer.close()    
    context={'image_base64':image_base64 }
    return render(request,'product/plot.html',context)

def salesPlot(request):

    labels = ['Freedom Ford', 'Westside Toyota', 'Go Honda', 'West Edmonton Hyundai', 'Crosstown Dodge']
    window_tint = [20, 35, 30, 35, 27]
    undercoating = [25, 32, 34, 20, 25]
    car_alarm = [10, 12, 18, 20, 22]
    film_3M = [5, 6, 4, 7, 5]
    rustproofing = [6, 3, 4, 10, 15]
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    fig, ax = plt.subplots()

    ax.bar(labels, window_tint, width, label='Window Tint')
    ax.bar(labels, undercoating, width, label='undercoating')
    ax.bar(labels, car_alarm, width, label='car_alarm')
    ax.bar(labels, film_3M, width, label='film_3M')
    ax.bar(labels, rustproofing, width, label='rustproofing')

    plt.setp(ax.get_xticklabels(), fontsize=6, rotation=18)
    ax.set_ylabel('Total Units')
    ax.set_title('Units of Product at Dealership')
    ax.legend()

    # Create a bytes buffer for saving image
    figbuffer = BytesIO()
    plt.savefig(figbuffer, format='png', dpi=350)
    image_base640=base64.b64encode(figbuffer.getvalue())
    image_base64 = image_base640.decode('utf-8')
    figbuffer.close()    
    context={'image_base64':image_base64 }
    return render(request,'product/sales_plot.html',context)
    
def edit_receipt(request, pk):
    """Edit an existing entry."""
    edit_item = Sale.objects.get(id = pk)   
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EditSaleForm(instance=edit_item)
    else:
        # POST data submitted; process data.
        form = EditSaleForm(instance=edit_item, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:receipt')    
    context = { 'form': form}
    return render(request, 'product/edit_receipt.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('', topic_id=topic.id)    
    context = {'entry': entry, 'edit': edit, 'form': form}
    return render(request, 'product/edit_entry.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('', topic_id=topic_id)
               
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'product/new_entry.html', context)

def warranty_homepage(request):
    products = Product.objects.all().order_by('id')
    return render(request, 'product/warranty_homepage.html', {
        'products': products})



