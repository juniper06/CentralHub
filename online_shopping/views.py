from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect

from online_shopping.models import Product, OrderItem


# Create your views here.


@login_required
def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "online_shopping/home.html", context=context)


@login_required
def cart(request):
    order_item_count = OrderItem.objects.not_placed_orders().filter(user=request.user).aggregate(order_item_count=Count('id'))[
        'order_item_count']

    order_items = OrderItem.objects.not_placed_orders().filter(user=request.user)
    total_amount = sum(order_item.sub_total for order_item in order_items)
    context = {
        'order_item_count': order_item_count,
        'order_items': order_items,
        'total_amount': total_amount
    }
    return render(request, "online_shopping/cart.html", context=context)


@login_required
def add_to_cart(request, product_id):
    try:
        order_item = OrderItem.objects.filter(user=request.user, product_id=product_id).first()
        if order_item:
            order_item.quantity += 1
        else:
            order_item = OrderItem(user=request.user, product_id=product_id)
        order_item.save()
        return redirect("home")
    except IntegrityError:
        return HttpResponse("Product ID Not Found!")

