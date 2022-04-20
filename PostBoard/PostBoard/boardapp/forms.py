from django.forms import ModelForm, BooleanField, CharField
from allauth.account.forms import SignupForm
from .models import Post, User, Author, Message


# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'category', 'text', 'image', 'author']
        labels = {
            'name': 'Название',
            'category': 'Категория',
            # 'is_news': 'Отметить, если новость',
            'text': 'Текст статьи',
            'image': 'Изображение/Видео',
            'author': 'Автор'

        }


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Username',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
        }


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        # basic_group = Group.objects.get(name='common')
        Author.user_set.add(user)
        return user


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        labels = {
            'text': 'Сообщение',
        }

