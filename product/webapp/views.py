from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, F
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View, TemplateView

from webapp.forms import ProductForm, OrderForm
from webapp.models import Product, Order

from webapp.models import Basket


class List_of_product_view(ListView):
    model = Product
    template_name = 'list_of_product_view.html'
    ordering = ('category', 'name')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(List_of_product_view, self).get_context_data(**kwargs)
        products = Product.objects.all().filter(remainder__gt=1)
        page = self.request.GET.get('page')
        query = self.request.GET.get('query', None)
        if query is not None:
            products = products.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        paginator = Paginator(products, self.paginate_by)

        try:
            product_pages = paginator.page(page)
        except PageNotAnInteger:
            product_pages = paginator.page(1)
        except EmptyPage:
            product_pages = paginator.page(paginator.num_pages)

        context['list_product'] = product_pages
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'product_view.html'
    context_object_name = 'products'
    pk_url_kwarg = 'pk'


class Create_Product(CreateView):
    form_class = ProductForm
    template_name = 'create_view.html'
    success_url = 'list'

    def form_valid(self, form):
        Product.objects.create(**form.cleaned_data)
        return redirect(self.success_url)


class UpdateProductView(UpdateView):
    form_class = ProductForm
    template_name = 'update_view.html'
    success_url = 'list'
    context_object_name = 'update'

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=id)

    def form_vali(self, form):
        Product.objects.create(**form.cleaned_data)
        return redirect(self.success_url)


class RemoveView(DeleteView):
    model = Product
    template_name = 'list_of_product_view.html'
    success_url = reverse_lazy('list')
    context_object_name = 'list_product'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class GoodOfBasket(TemplateView):
    model = Basket
    template_name = 'basket_add.html'
    context_object_name = 'baskets'
    success_url = 'list'

    def get(self,*args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)

        if product.remainder > 0:
            try:
                cart = Basket.objects.get(product__id=product.pk)
                product.remainder -= 1
                cart.amount += 1
                product.save()
                cart.save()
            except:
                Basket.objects.get_or_create(product=product, amount=1)
                product.remainder -= 1
                product.save()
            return redirect('list')

        return redirect('list')


class BasketList(ListView):
    model = Basket
    template_name = 'basket-list.html'
    context_object_name = 'basket_list'
    success_url = 'list'

    def add(self,**kwargs):
        list_bask = Basket.objects.all()
        summa = 0
        for s in list_bask:
            summa += s.amount * s.product.price
        return summa

    def get_context_data(self,**kwargs):
        context = super().get_context_data( **kwargs)
        list_bask = Basket.objects.all()
        total = []
        for s in list_bask:
            total.append({'b': s, 'total': s.amount * s.product.price})

        context['summa'] = self.add()
        context['baskets'] = total
        return context


class OrderList(CreateView):
    model = Order
    template_name = 'form-order.html'
    success_url = 'list'
    form_class = OrderForm
    context_object_name = 'form'

    def form_valid(self, form):
        Order.objects.create(**form.cleaned_data)
        return redirect(self.success_url)


class BasketDelete(DeleteView):
    model = Basket
    template_name = 'basket-list.html'
    success_url = reverse_lazy('basket-list')
    context_object_name = 'baskets'

    def get(self, request, *args, **kwargs):
        basket = self.get_object()
        product = basket.product
        product.remainder += basket.amount
        product.save()
        return self.delete(request, *args, **kwargs)


