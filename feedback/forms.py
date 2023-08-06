from django import forms
from .models import UserFeedback


class feedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['name', 'today_date', 'category', 'product',
                  'rating', 'purchase_date', 'description']
