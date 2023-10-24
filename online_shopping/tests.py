from django.test import TestCase

from accounts.models import User
from online_shopping.models import Product, OrderItem, Category


# Create your tests here.


class OnlineShoppingTestCase(TestCase):
    def test_product_cart(self):
        jeans = Category.objects.create(name="jeans")
        shirt = Category.objects.create(name="shirt")

        product1 = Product.objects.create(name='Blue Jeans', price=10.0,
                                         description="The best thing about choosing a blue jeans outfit for men is "
                                                     "that you can club it with almost anything. You can go with "
                                                     "neutral color like white shirts, or you can pump the look with "
                                                     "a printed silk shirt. There is no boundary to limit your "
                                                     "choices, you can also choose any style of jeans.")
        product1.categories.add(jeans)
        self.assertEqual(product1.name, 'Blue Jeans')

        product2 = Product.objects.create(name='T-Shirt V-neck', price=20.0,
                                         description="The best thing about choosing a blue jeans outfit for men is "
                                                     "that you can club it with almost anything. You can go with "
                                                     "neutral color like white shirts, or you can pump the look with "
                                                     "a printed silk shirt. There is no boundary to limit your "
                                                     "choices, you can also choose any style of jeans.")
        product2.categories.add(shirt)
        self.assertEqual(product2.name, 'T-Shirt V-neck')

        earlfunk21 = User.objects.create(email="earlnobe@email.com", first_name="earl", last_name="funk")
        earlfunk21.set_password("123123")
        cart = Cart.objects.create(user=earlfunk21)

        self.assertEqual(earlfunk21.cart, cart)

        OrderItem.objects.create(cart=cart, product=product1, quantity=1)
        OrderItem.objects.create(cart=cart, product=product2, quantity=2)

        cart_items = cart.cartitem_set.all()

        total_price = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)
        self.assertEqual(total_price, 50.0)
