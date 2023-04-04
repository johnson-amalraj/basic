from django.views.generic import ListView
from .models import Product

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
