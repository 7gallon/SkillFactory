from django.views.generic import ListView, DetailView
from .models import Post


class PostView(ListView):
    model = Post
    template_name = 'newslist.html'
    context_object_name = 'newslist'


class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
