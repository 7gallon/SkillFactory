from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author, Category, PostCategory, CategoryUser
from django.contrib.auth.models import User
from .filters import PostFilter
from .forms import NewsForm, ProfileForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
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
        # cat_ids = PostCategory.objects.all().values('id')
        # print(Category.objects.filter(id = cat_ids).values('name'))
        # context['news_in_category'] = Category.objects.filter(id = cat_ids).values('name')
        return context


class CategoryPostView(ListView):
    model = Post
    template_name = 'newslist.html'
    context_object_name = 'Category_newslist'
    ordering = ['-time_emerged']
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self,  **kwargs):
        id = self.kwargs.get('pk')
        # print(id)
        postcat_obj = PostCategory.objects.filter(post=id)
        # print(postcat_obj)
        user_obj = self.request.user
        # cat = postcat_obj.category
        context = super().get_context_data(**kwargs)
        for cat in postcat_obj:
            context['is_subscribed'] = Category(id=cat.category.id).subscribers.filter(username=user_obj).exists()
        context['cat_obj'] = PostCategory.objects.filter(post=id)
        return context


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

    def form_valid(self, form):
    # def post(self, request, *args, **kwargs):
        html_content = render_to_string(
            'news_msg.html',
        )
        # category_id = 1
        category_id = self.request.POST.get('category')
        post_text = self.request.POST.get('text')
        post_name = self.request.POST.get('name')
        text_content = f' | {post_name} | \n{post_text[:50]}...'
        print(f'category_id {category_id}')
        print(f'CategoryUser.objects {CategoryUser.objects.filter(category=category_id).values("user_id")}')
        cat_subscribers_obj = CategoryUser.objects.filter(category=category_id).values('user_id')
        print(f'cat_subscribers_obj {cat_subscribers_obj}')
        for suber_id in cat_subscribers_obj:
            suber = User.objects.get(id=suber_id['user_id'])
            print(suber)
            msg = EmailMultiAlternatives(
                subject=f'News update on you favourite categories',
                # body=f'{post_text[:50]}',
                body='post_name post_text',
                from_email='sev7engallon@yandex.ru',
                to=[suber.email]
            )
            # msg.attach_alternative(html_content, "text/html")
            msg.attach_alternative(text_content, "text/plain")
            msg.send()
        return super().form_valid(form)


class NewsUpdateView(UpdateView, PermissionRequiredMixin):
    permission_required = ('news.change_post', )
    template_name = 'news_add.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления
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


@login_required
def subscribe_me(request, **kwargs):
    user_obj = request.user
    # print(user_obj)
    id = kwargs.get('pk')
    # print(id)
    category_obj = Category.objects.get(id=id)
    # print(Category.objects.get(id=id))
    # c_user = category_obj.user
    if not category_obj.subscribers.filter(username=user_obj).exists():
        category_obj.subscribers.add(user_obj)
    return redirect('news_detail', pk=id)
