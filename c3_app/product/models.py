from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# need to implement access control 
class Category(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete = models.CASCADE,null = True, blank = True )
    item_name = models.CharField(max_length = 50, null = True, blank = True)
    total_quantity = models.IntegerField(default = 0, null = True, blank = True)
    issued_quantity = models.IntegerField(default = 0, null = True, blank = True)
    received_quantity = models.IntegerField(default = 0, null = True, blank = True)
   
    def __str__(self):
        return self.item_name

class Sale(models.Model):
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    car_dealership = models.CharField(max_length = 50, null = True, blank = True)
   
    def __str__(self):
        return self.item.item_name

class Edit(models.Model):

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
    # Return a string representation of the model
        return self.text

class Entry(models.Model):

    topic = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, blank = True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name_plural = 'my warranty entries'

        def __str__(self):
        # Return a string representation of the model    
            return f"{self.text[:50]}..."
