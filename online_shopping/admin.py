from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['category']
    fieldsets = [
        (None, {
            'fields': [
                'name',
                'description',
                'price',
                'category',
                'image'

            ],

        }),
    ]


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


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


# Register your models here.
admin.site.register(models.OrderItem, OrderItemAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)
