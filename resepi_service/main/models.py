from django.db import models
from django.urls import reverse


class User(models.Model):
    Name = models.CharField(max_length=30, blank=False)
    Sername = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.Name}, {self.Sername}'

class Recipe(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('recipe', kwargs={'recipe_slug': self.slug})

    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'
        ordering = ['-time_create', 'title']


class Categories(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категории рецептов'
        verbose_name_plural = 'Категории рецептов'