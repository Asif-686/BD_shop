from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name = models.CharField (max_length=80,unique=True)
    slug = models.CharField( max_length=120, unique=True)
    description = models.TextField(blank=True)
    category_iamge = models.ImageField(upload_to ='images/photos/')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_urls(self):
        return reverse('by_name',args=[self.slug])
        
    def __str__(self):
        return str(self.category_name)

