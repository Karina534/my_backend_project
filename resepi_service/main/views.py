from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import *

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'data', '123'],
    }
    return render(request, 'main/index.html')

def recipeGenerator(request):
    return render(request, 'main/recipeGenerator.html')

def recipeList(request):
    return render(request, 'main/recipeList.html')

def byKitchen(request):
    return render(request, 'main/byKitchen.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def recipes(request):
    recipes = Recipe.objects.all()
    category = Categories.objects.all()
    context = {
        'recipes': recipes,
        'title': 'Рецепты',
        'category': category,
        'category_selected': 0,
    }
    return render(request, 'main/recipes.html', context=context)

def support(request):
    return render(request, 'main/support.html')

def show_recipe(request, recipe_id):
    return HttpResponse(f'Отображение рецепта с id: {recipe_id}')
def show_category(request, category_id):
    recipes = Recipe.objects.filter(category_id=category_id)
    category = Categories.objects.all()

    if len(recipes) == 0:
        raise Http404()

    context = {
        'recipes': recipes,
        'title': 'Категории',
        'category': category,
        'category_selected': category_id,
    }
    return render(request, 'main/recipes.html', context=context)