from django.contrib import admin

from webapp.models import Product,Basket,Order

admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Order)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category']

    list_filter = ['name']

    search_fields = ['name', 'description']

    fields = ['name', 'description', 'category', 'remainder', 'price']

    readonly_fields = ['remainder', 'price']
