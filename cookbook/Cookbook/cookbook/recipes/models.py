from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name.title()}'


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    ingredients = models.TextField()
    description = models.TextField()
    author = models.ForeignKey('Author', related_name='recipes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title.title()}'


