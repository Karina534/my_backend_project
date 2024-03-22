from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import show_recipe, show_category

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('recipeGenerator', views.recipeGenerator, name='recipeGenerator'),
    path('recipeList', views.recipeList, name='recipeList'),
    path('byKitchen', views.byKitchen, name='byKitchen'),
    path('recipes', views.recipes, name='recipes'),
    path('support', views.support, name='support'),
    path('recipe/<slug:recipe_slug>/', show_recipe, name='recipe'),
    path('category/<slug:category_slug>/', show_category, name='category'),
    path('add_recipe', views.add_recipe, name="add_recipe")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)