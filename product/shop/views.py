from django.shortcuts import render, redirect, get_object_or_404
from .models import Product,OrderItem
from django.contrib.auth.decorators import login_required

# List products / home
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, "product_form.html", {"products": products})

@login_required
def view(request):
     order = OrderItem.objects.filter(user=request.user)
     total= sum(item.product.price*item.qty for item in order)
     return render(request,"cart.html",{"order":order,"total":total})

# Add product
@login_required
def add_product(request,product_id):
        product=Product.objects.get(id=product_id)
        order,create= OrderItem.objects.get_or_create(product=product)
        order.qty+=1
        order.save()
        return redirect("view")

# Delete product
@login_required
def delete_product(request, product_id):
    product = get_object_or_404(OrderItem, id=product_id)
    product.delete()
    return redirect("view")  # Redirect instead of render

