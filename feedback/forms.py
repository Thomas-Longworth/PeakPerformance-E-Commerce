from django import forms
from .models import UserFeedback


class feedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['name', 'category', 'product', 'rating', 'description']
