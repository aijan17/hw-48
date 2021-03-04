from django.contrib import admin

from webapp.models import Product

admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category']

    list_filter = ['name']

    search_fields = ['name', 'description']

    fields = ['name', 'description', 'category', 'remainder', 'price']

    readonly_fields = ['remainder', 'price']
