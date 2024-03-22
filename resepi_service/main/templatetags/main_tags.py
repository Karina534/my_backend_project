from django import template
from main.models import *

register = template.Library()

@register.simple_tag
def get_categories():
    return Categories.objects.all()

@register.inclusion_tag('main/recipe_category_tag.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        category = Categories.objects.all()
    else:
        category = Categories.objects.sort(sort)
    return {'category':category, 'category_selected': category_selected}