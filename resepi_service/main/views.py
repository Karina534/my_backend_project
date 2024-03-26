from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView

from .forms import AddRecipeForm
from .models import *


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_recipe'},
        {'title': 'Главная', 'url_name': 'home'}
        ]

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

class RecipeHome(ListView):
    model = Recipe
    template_name = 'main/recipes.html'
    context_object_name = 'recipes'
    extra_context = {'title': 'Добавление страницы'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['category_selected'] = 0
        return context

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True)

'''def recipes(request):
    recipes = Recipe.objects.all()
    #category = Categories.objects.all()
    context = {
        'recipes': recipes,
        'title': 'Рецепты',
        #'category': category,
        'category_selected': 0,
    }
    return render(request, 'main/recipes.html', context=context)'''

def support(request):
    return render(request, 'main/support.html')

class ShowRecipe(DeleteView):
    model = Recipe
    template_name = 'main/post.html'
    slug_url_kwarg = 'recipe_slug'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

'''def show_recipe(request, recipe_slug):
    post = get_object_or_404(Recipe, slug=recipe_slug)
    context = {
        'post': post,
        #'menu': menu,
        'title': post.title,
        'category_selected': post.category_id,
    }
    return render(request, 'main/post.html', context=context)
    #return HttpResponse(f'Отображение рецепта с id: {recipe_id}')'''

class RecipeCategory(ListView):
    model = Recipe
    template_name = 'main/recipes.html'
    context_object_name = 'recipes'
    allow_empty = False
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['recipes'][0].category)
        context['menu'] = menu
        context['category_selected'] = context['recipes'][0].category_id
        return context
    def get_queryset(self):
        return Recipe.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)


'''def show_category(request, category_slug):
    #category = Categories.objects.all()
    recipes = get_object_or_404(Categories, slug=category_slug)
    posts = Recipe.objects.filter(category_id=recipes.pk)

    context = {
        'recipes': posts,
        'title': 'Категории',
        #'category': category,
        'category_selected': posts[0].id,
    }
    return render(request, 'main/recipes.html', context=context)'''

class AddPage(CreateView):
    form_class = AddRecipeForm
    template_name = 'main/add_recipe.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление рецепта'
        context['menu'] = menu
        return context

'''def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("recipes")
    else:
        form = AddRecipeForm()
    return render(request, 'main/add_recipe.html', {'title': 'Добавление статьи', 'form': form})'''