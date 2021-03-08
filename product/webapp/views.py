
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import ProductForm
from webapp.models import Product


def list_of_product_view(request):
    list_product = Product.objects.all().filter(remainder__gt=1).order_by('category', 'name')
    return render(request, 'list_of_product_view.html', {"list_product": list_product})


def product_view(request, id):
    products = Product.objects.get(id=id)
    return render(request, 'product_view.html', {'products': products})


def get_queryset(request):
    query = request.GET['query']
    list_product = Product.objects.all().filter(remainder__gt=1).order_by('category', 'name')
    if query:
        list_product = Product.objects.filter(name__icontains=query)

    return render(request, 'list_of_product_view.html', {"list_product": list_product})


def create_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create_view.html', context={'form': form})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                category=form.cleaned_data.get('category'),
                remainder=form.cleaned_data.get('remainder'),
                price=form.cleaned_data.get('price')
            )
            return redirect('list')
        return render(request, 'create_view.html', context={'form': form})


def update_view(request, id):
    update = get_object_or_404(Product, id=id)

    if request.method == 'GET':
        form = ProductForm(initial={
            'name': update.name,
            'description': update.description,
            'category': update.category,
            'remainder': update.remainder,
            'price': update.price
        })
        return render(request, 'update_view.html', context={'form': form, 'update': update})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            update.name = form.cleaned_data.get("name")
            update.description = form.cleaned_data.get("description")
            update.category = form.cleaned_data.get("category")
            update.remainder = form.cleaned_data.get("remainder")
            update.price = form.cleaned_data.get('price')
            update.save()
            return redirect('list')

        return render(request, 'create_view.html', context={'form': form})


def remove_view(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'GET':
        product.delete()
    return redirect('list')


