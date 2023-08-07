from django import forms
from .models import UserFeedback

from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'


class feedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['name', 'made_on', 'product',
                  'rating', 'description']
        widgets = {
            'made_on': DateInput(),
        }
