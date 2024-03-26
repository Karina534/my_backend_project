from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('recipeGenerator', views.recipeGenerator, name='recipeGenerator'),
    path('recipeList', views.recipeList, name='recipeList'),
    path('byKitchen', views.byKitchen, name='byKitchen'),
    path('recipes', RecipeHome.as_view(), name='recipes'),
    path('support', views.support, name='support'),
    path('recipe/<slug:recipe_slug>/', ShowRecipe.as_view(), name='recipe'),
    path('category/<slug:category_slug>/', RecipeCategory.as_view(), name='category'),
    path('add_recipe', AddPage.as_view(), name="add_recipe")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)