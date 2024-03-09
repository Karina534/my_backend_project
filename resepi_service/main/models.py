from django.db import models

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
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title