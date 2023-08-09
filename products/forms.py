from django import forms
from .models import Product, Category, Question
from django import forms

from django.forms import ModelForm


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class DateInput(forms.DateInput):
    input_type = 'date'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['date_on', 'question']
        widgets = {
            'date_on': DateInput(),
        }
