from django.db import models
from cloudinary.models import CloudinaryField

from django.db import models
from profiles.models import UserProfile
from django.forms import ModelForm
from django.contrib.auth.models import User

from datetime import datetime, date


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    question = models.CharField(
        max_length=254, default='Ask your question here')

    date_on = models.DateField(default=date.today)

    def __str__(self):
        return self.question


