from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddRecipeForm
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
    #category = Categories.objects.all()
    context = {
        'recipes': recipes,
        'title': 'Рецепты',
        #'category': category,
        'category_selected': 0,
    }
    return render(request, 'main/recipes.html', context=context)

def support(request):
    return render(request, 'main/support.html')

def show_recipe(request, recipe_slug):
    post = get_object_or_404(Recipe, slug=recipe_slug)
    context = {
        'post': post,
        #'menu': menu,
        'title': post.title,
        'category_selected': post.category_id,
    }
    return render(request, 'main/post.html', context=context)
    #return HttpResponse(f'Отображение рецепта с id: {recipe_id}')
def show_category(request, category_slug):
    #category = Categories.objects.all()
    recipes = get_object_or_404(Categories, slug=category_slug)
    posts = Recipe.objects.filter(category_id=recipes.pk)

    context = {
        'recipes': posts,
        'title': 'Категории',
        #'category': category,
        'category_selected': posts[0].id,
    }
    return render(request, 'main/recipes.html', context=context)

def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Recipe.objects.create(**form.cleaned_data)
                return redirect("recipes")
            except:
                form.add_error(None, 'Ошибка создания рецепта')
    else:
        form = AddRecipeForm()
    return render(request, 'main/add_recipe.html', {'title': 'Добавление статьи', 'form': form})