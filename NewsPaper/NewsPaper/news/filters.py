from django_filters import FilterSet, CharFilter, DateFilter
from .models import Post
from django.forms import DateInput


class PostFilter(FilterSet):
        author = CharFilter(
            field_name='author__user__username',
            lookup_expr='icontains',
            label='Автор'
        )

        title = CharFilter(
            field_name='name',
            lookup_expr='icontains',
            label='Название статьи'
        )
        datetime = DateFilter(
            field_name='time_emerged',
            widget=DateInput(attrs={'type': 'date'}),
            lookup_expr='gt',
            label='Позже даты'
        )

        class Meta:
            model = Post
            fields = []

                # {
                # 'name': ['icontains'],
                # 'time_emerged': ['gt'],
                # 'author__user__username': ['icontains'],
                # }
                #
