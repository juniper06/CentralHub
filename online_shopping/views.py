from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from online_shopping.models import Product, OrderItem, Category


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
    order_item_count = \
        OrderItem.objects.not_placed_orders().filter(user=request.user).aggregate(order_item_count=Count('id'))[
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


@login_required
def product_details(request, slug):
    try:
        product = Product.objects.filter(slug=slug).first()
        context = {
            "product": product
        }
        return render(request, "online_shopping/product.html", context=context)
    except IntegrityError:
        return HttpResponse("Product Not Found!")


@login_required
def shop_view(request):
    search = request.GET.get('search', '')
    category = request.GET.get("category", None)
    if category is not None:
        products = Product.objects.filter(category__name=category).all()
    else:
        products = Product.objects.all().filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__name__icontains=search)).order_by(
            "-created_at")
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)
    categories = Category.objects.all()
    context = {
        'page': page,
        'categories': categories,
    }
    return render(request, "online_shopping/shop.html", context)
