from django import forms
from .models import Refund

from django.forms import ModelForm


class refundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ['name', 'product', 'orderkey',
                  'reason', 'explaination']
