from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=6)
    size = models.CharField(max_length=255)
    category =models.ForeignKey('Category',on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    created_to = models.ForeignKey(User,on_delete = models.CASCADE)
    complete = models.BooleanField(default=False)

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL , null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    


