from django.shortcuts import render

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