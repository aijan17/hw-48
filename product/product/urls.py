"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import List_of_product_view, ProductView, Create_Product, RemoveView, UpdateProductView, BasketDelete

from webapp.views import GoodOfBasket,BasketList,OrderList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List_of_product_view.as_view(), name='list'),
    path('product/<int:pk>', ProductView.as_view(), name='product-view'),
    path('add/', Create_Product.as_view(), name='add'),
    path('remove/<int:pk>', RemoveView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update'),
    path('basket/<int:pk>',GoodOfBasket.as_view(),name='basket'),
    path('basket/list/', BasketList.as_view(),name='basket-list'),
    path('order/',OrderList.as_view(),name='order'),
    path('basket/remove/<int:pk>',BasketDelete.as_view(),name='del-basket')
]