from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q, Sum, F
from django.shortcuts import render, get_object_or_404, redirect

from accounts.models import User
from dashboard.forms import ProductForm, CategoryForm
from online_shopping.models import Product, Order, Category


# Create your views here.

def is_staff(user: User):
    return user.is_staff


@user_passes_test(is_staff)
def overview(request):
    total_users = User.objects.count()
    total_products = Product.objects.count()
    total_sales = Order.objects.aggregate(total=Sum(F('items__quantity') * F('items__product__price')))['total'] or 0
    total_ordered = Order.objects.count()
    context = {
        'total_sales': total_sales,
        'total_users': total_users,
        'total_products': total_products,
        'total_ordered': total_ordered,
    }
    return render(request, "dashboard/overview.html", context=context)


@user_passes_test(is_staff)
def product_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added")
            return redirect("product")
    else:
        form = ProductForm()

    search = request.GET.get('search', '')
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
        'form': form,
        'categories': categories,
    }
    return render(request, "dashboard/product.html", context=context)


@user_passes_test(is_staff)
def delete_product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect("product")


@user_passes_test(is_staff)
def category_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added")
            return redirect("category")
    categories = Category.objects.all()
    paginator = Paginator(categories, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)
    context = {
        'page': page,
    }
    return render(request, "dashboard/category.html", context)


@user_passes_test(is_staff)
def orders_view(request):
    search = request.GET.get('search', '')
    orders = Order.objects.all().filter(
        Q(status__icontains=search) |
        Q(user__email__icontains=search)).order_by(
        "-date_ordered")
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)
    context = {
        'page': page,
    }
    return render(request, "dashboard/orders.html", context)


@user_passes_test(is_staff)
def update_status(request, order_id):
    status = request.GET.get('status')
    order = get_object_or_404(Order, id=order_id)
    order.update_status(status)
    messages.success(request, "Successfully Updated")
    return redirect("orders")
