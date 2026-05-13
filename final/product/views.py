from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


def read_product(request):
    products = Product.objects.all()
    max_product = max(products, key=lambda p: p.total, default=None)
    return render(request, 'read_product.html', {
        'products': products,
        'max_product': max_product,
    })


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return render(request, 'create_product.html', {
                'created': True,
                'product': product,
            })
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form, 'created': False})


def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/product/read')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('/product/read')
    return render(request, 'delete_product.html', {'product': product})
