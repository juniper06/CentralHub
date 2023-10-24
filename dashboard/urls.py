from django.contrib.auth.decorators import login_required
from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.overview, name="overview"),
    path('product', views.product_view, name="product"),
    path('delete_product/<int:product_id>', views.delete_product_view, name="delete_product"),
    path('category', views.category_view, name="category")
]
