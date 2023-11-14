from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', default='images/no-image.png')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + str(self.id))
        super().save(*args, **kwargs)


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

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return self.user.get_username()

    @property
    def total_amount(self):
        return self.items.aggregate(total=models.Sum(models.F('quantity') * models.F('product__price')))['total'] or 0

    def update_status(self, new_status):
        if new_status in dict(self.STATUS_CHOICES):
            self.status = new_status
            self.save()
        else:
            raise ValueError(f"Invalid status: {new_status}")