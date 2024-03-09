from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import show_recipe

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('recipeGenerator', views.recipeGenerator, name='recipeGenerator'),
    path('recipeList', views.recipeList, name='recipeList'),
    path('byKitchen', views.byKitchen, name='byKitchen'),
    path('recipes', views.recipes, name='recipes'),
    path('support', views.support, name='support'),
    path('recipe/<int:recipe_id>/', show_recipe, name='recipe')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)