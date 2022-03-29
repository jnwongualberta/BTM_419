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

]