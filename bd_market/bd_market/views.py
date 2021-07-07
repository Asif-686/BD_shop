from django.shortcuts import render
from Store.models import Product
def index(request):
    products = Product.objects.all().filter(is_available = True)

    content = {
                'products': products,
               }
      
    return render(request,'index.html',content)
