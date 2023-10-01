from django.core.validators import MinValueValidator
from django.db import models

from accounts.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    sold = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    @property
    def category_list(self):
        return ', '.join([category.name for category in self.categories.all()])


class OrderItemManager(models.Manager):
    def not_placed_orders(self):
        return self.filter(order__isnull=True)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    objects = OrderItemManager()

    def __str__(self):
        return f"{self.product.name} = {self.quantity}"

    @property
    def sub_total(self):
        return self.product.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_username()

    @property
    def total_amount(self):
        return self.items.aggregate(total=models.Sum(models.F('quantity') * models.F('product__price')))['total'] or 0
