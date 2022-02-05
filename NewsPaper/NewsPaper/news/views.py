from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author
from django.contrib.auth.models import User
from .filters import PostFilter
from .forms import NewsForm, ProfileForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator


class PostView(ListView):
    model = Post
    template_name = 'newslist.html'
    context_object_name = 'newslist'
    ordering = ['-time_emerged']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authed'] = self.request.user.is_authenticated
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


class PostSearch(ListView):
    model = Post
    template_name = 'newssearch.html'
    context_object_name = 'newssearch'
    ordering = ['-time_emerged']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsAddView(CreateView, PermissionRequiredMixin):
    permission_required = ('news.add_post', )
    template_name = 'news_add.html'
    form_class = NewsForm


class NewsUpdateView(UpdateView, PermissionRequiredMixin):
    permission_required = ('news.change_post', )
    template_name = 'news_add.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class NewsDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/newslist/'


class AuthorDetail(DetailView,):
    model = Author
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authed'] = self.request.user.is_authenticated
        context['curr_user'] = self.request.user.id
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile_update.html'
    form_class = ProfileForm
    success_url = '/newslist/'
    # id = Author
    # success_url = reverse_lazy('author_detail', args=[User.objects.get(username =id).id])

    def get_object(self, **kwargs):
        cur_user = self.request.user
        # if self.request.user.is_authenticated:
        id = self.kwargs.get('pk')
        return User.objects.get(pk=id)
        # else:
        #     return redirect('/accounts/login/')


@login_required
def make_author(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')
