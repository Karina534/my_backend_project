from django import forms
from .models import *

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=150, label="Заголовок")
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Рецепт")
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), label="Категория", empty_label="Категория не выбрана")
    is_published = forms.BooleanField(required=False, label="Опубликовать", initial=True)