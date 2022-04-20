from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f'{self.user.username.title()}'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return f'{self.title.title()}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    time_emerged = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    category = models.ManyToManyField(Category, through='PostCategory')
    name = models.CharField(max_length=255, verbose_name='Название')
    text = RichTextUploadingField(null = True)
    liked = models.ManyToManyField(User, through='PostUser')
    image = models.FileField(null=True)

    def __str__(self):
        return f'{self.name.title()}: {self.preview()}'

    def preview(self):
        return self.text[:124] + '...'

    def like(self):
        if not self.liked:
            self.liked = True
            self.save()

    def get_absolute_url(self):
        return f'/board/{self.pk}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Message(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_emerged = models.DateTimeField(auto_now_add=True)
    submitted = models.BooleanField(default=False)

    def submit(self):
        self.submitted = True
        self.save()


class PostUser(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
