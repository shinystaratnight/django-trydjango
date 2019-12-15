from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../products')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)