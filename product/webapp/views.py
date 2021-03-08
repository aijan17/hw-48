from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404

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