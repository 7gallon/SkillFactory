from django.forms import ModelForm, BooleanField, MultipleChoiceField
from .models import Post, Author
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


# Создаём модельную форму
class NewsForm(ModelForm):
    class Meta:
        is_news = BooleanField(label='Отметьте, если это новость: ')
        model = Post
        fields = ['name', 'category', 'is_news', 'text', 'author']
        labels = {
            'name': 'Название',
            'category': 'Категория',
            'is_news': 'Отметить, если новость',
            'text': 'Текст статьи',
            'author': 'Автор',
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
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
