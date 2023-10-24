from django.forms import models, Select

from online_shopping.models import Product, Category


class ProductForm(models.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "image", "category"]
        widgets = {
            'category': Select(attrs={'class': 'form-select', 'required': 'false'})
        }


class CategoryForm(models.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
