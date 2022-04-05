from django.urls import path
from product import views
from django.contrib.auth import views as auth_views

app_name = 'product'

urlpatterns = [
    path('', views.home, name = "home"),
    path('receipt/', views.receipt, name = "receipt"),
    path('receipt/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'), 
    path('home/<int:product_id>/', views.product_detail, name='product_detail'),
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),   
    path('add_to_inventory/<str:pk>/', views.add_to_inventory, name='add_to_inventory'),
    path('all_sales/', views.all_sales, name = 'all_sales'),
    path('inventory/', views.inventory, name = 'inventory'),
    path('add_new_inventory/', views.add_new_inventory, name = 'add_new_inventory'),
    path('edit_inventory/<str:pk>/', views.edit_inventory, name = 'edit_inventory'),
    path('add_category/', views.add_category, name = 'add_category'),
    path('plot',views.plot,name='plot'),
    path('salesPlot',views.salesPlot,name='salesPlot'),
    path('edit_receipt/<str:pk>/', views.edit_receipt, name = 'edit_receipt'),
    path('new_entry/<int:topic_id>',views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('warranty_homepage/', views.warranty_homepage, name='warranty_homepage'),
]