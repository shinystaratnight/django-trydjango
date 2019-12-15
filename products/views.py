from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list_view(request):
    queryset = Product.objects.all()    # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)