from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category_list', 'sold']
    list_filter = ['sold', 'categories']
    fieldsets = [
        (None, {
            'fields': [
                'name',
                'description',
                'price',
                'sold',
                'categories',

            ],

        }),
    ]
    filter_horizontal = ['categories']


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "total_amount", "date_ordered"]

    fieldsets = [
        (None, {
            'fields': [
                'user',
                'items',
            ],
        }),
    ]

    filter_horizontal = ['items']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "quantity"]


# Register your models here.
admin.site.register(models.OrderItem, OrderItemAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)
