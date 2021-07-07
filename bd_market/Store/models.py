from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
     product_name = models.CharField(max_length=200 ,unique=True)
     slug = models.CharField(max_length=200,unique=True)
     description = models.TextField(blank=True,max_length=350)
     price = models.IntegerField()
     stock = models.IntegerField()
     images = ImageField(upload_to = 'images/productimages/')
     is_available = models.BooleanField(default=True)
     category = models.ForeignKey(Category,on_delete=CASCADE)
     created_date = models.DateTimeField(auto_now_add=True)
     modified_date = models.DateTimeField(auto_now=True)

     def get_urls(self):
        return reverse('product_details', args=[self.category.slug, self.slug])

     def __str__(self):
         return self.product_name
 
