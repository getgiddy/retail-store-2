from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product} in {self.cart}"


ORDER_STATUSES = (
    ("n", "new"),
    ("t", "transit"),
    ("d", "delivered"),
    ("c", "cancelled"),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1, choices=ORDER_STATUSES, default='n')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Order"


class OrderItem(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product} in {self.order}"


class Product(models.Model):
    name = models.CharField(max_length=124)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(
        upload_to='product_images', default='default.png')

    def __str__(self):
        return self.name
