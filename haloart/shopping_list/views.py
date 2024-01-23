from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    filter_param = request.GET.get('filter')
    sort_param = request.GET.get('sort')

    # Apply the filter and sort if they exist
    if filter_param:
        products = products.filter(name__icontains=filter_param)
    if sort_param:
        products = products.order_by(sort_param)
    return render(
        request, 'products/product_list.html', {'products': products}
        )

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('shopping_list:product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'products/product_edit.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('shopping_list:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_edit.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('shopping_list:product_list')
    return render(request, 'products/product_delete.html', {'product': product})
