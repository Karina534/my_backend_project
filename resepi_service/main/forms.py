from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']
        widgets={
            'title': forms.TextInput(attrs={'class': 'title-input'}),
            'content': forms.Textarea(attrs={'class': 'content-area'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 255:
            raise ValidationError('Длина заголовка не может превышать 255 символов')
        return title