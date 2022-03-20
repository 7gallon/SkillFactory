from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache

from django.contrib.auth.base_user import AbstractBaseUser


# class User(AbstractBaseUser):
#     class Meta:
#         verbose_name = ('Пользователь')


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Автор')
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = Post.objects.filter(author__user__username=self.user.username).values('rating')
        comment_rating = Comment.objects.filter(user__username=self.user.username).values('rating')
        com_to_posts_rating = Comment.objects.filter(post__author__user__username=self.user.username).values('rating')
        self.rating = 0
        for p in posts_rating:
            self.rating += p['rating']*3
        for c in comment_rating:
            self.rating += c['rating']
        for cp in com_to_posts_rating:
            self.rating += cp['rating']
        self.save()

    def __str__(self):
        return f'{self.user.username.title()}'

    # def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
    #     return f'/newslist/profile/{self.id}'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, through='CategoryUser')

    def __str__(self):
        return f'{self.name.title()}'


class CategoryUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    is_news = models.BooleanField(default=True)
    time_emerged = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    category = models.ManyToManyField(Category, through='PostCategory')
    name = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def preview(self):
        return self.text[:124] + '...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.name.title()}: {self.preview()}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/newslist/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}') # затем удаляем его из кэша, чтобы сбросить его


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_emerged = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


