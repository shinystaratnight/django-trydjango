from django.shortcuts import render
from .models import Product

def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)