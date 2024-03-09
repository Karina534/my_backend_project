from django.http import HttpResponse
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
    return render(request, 'main/recipes.html', {'recipes': recipes, 'title': 'Рецепты'})

def support(request):
    return render(request, 'main/support.html')

def show_recipe(request, recipe_id):
    return HttpResponse(f'Отображение рецепта с id: {recipe_id}')