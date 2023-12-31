from django.db import models
from django.contrib.auth.models import User
from products.models import Category, Product

# Create your models here.


class Refund(models.Model):

    name = models.CharField(max_length=254)

    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.SET_NULL)

    orderkey = models.CharField(max_length=254)

    REASON_CHOICES = [
        (1, 'Product quality:'),
        (2, 'Late delivery'),
        (3, 'Misleading description'),
        (4, 'Billing error'),
        (5, 'Size issue'),

    ]

    reason = models.IntegerField(choices=REASON_CHOICES, default=1)

    explaination = models.CharField(max_length=254)

    def __str__(self):
        return self.name
