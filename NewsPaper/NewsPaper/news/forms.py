from django.forms import ModelForm, BooleanField
from .models import Post


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


