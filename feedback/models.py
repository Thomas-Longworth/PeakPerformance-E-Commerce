from django.db import models
from products.models import Category, Product
from datetime import datetime, date


class UserFeedback(models.Model):
    name = models.CharField(max_length=254)

    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)

    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.SET_NULL)

    today_date = models.DateField(default=date.today)

    RATING_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Fair'),
        (4, '4 - Average'),
        (5, '5 - Good'),
        (6, '6 - Above Average'),
        (7, '7 - Very Good'),
        (8, '8 - Excellent'),
        (9, '9 - Outstanding'),
        (10, '10 - Perfect'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES, default=5)

    description = models.TextField()

    purchase_date = models.DateField(default=date.today)

    def __str__(self):
        return self.name
