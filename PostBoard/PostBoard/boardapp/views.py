from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author, Message, User
from django.contrib.auth.models import User
from .filters import PostFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import PostForm, ProfileForm, MessageForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save, sender=Message)
def notify_message(sender, instance, created, **kwargs):

    if instance.submitted:
        subject = f'Здравствуйте, {instance.user.username}. '
        message = f'Ваше сообщение просмотрено/принято'
        send_mail(
            subject=subject,
            message=message,
            from_email='sev7engallon@yandex.ru',
            recipient_list=[instance.user.email]
        )

    subject = f'Здравствуйте, {instance.post.author.username}. '
    message = f'Вам пришел новый отклик на пост'
    send_mail(
        subject=subject,
        message=message,
        from_email='sev7engallon@yandex.ru',
        recipient_list=[instance.post.author.email]
    )


@receiver(post_save, sender=Post)
def notify_new_post(sender, instance, created, **kwargs):

    for user in User.objects.all():
        subject = f'Здравствуйте, {instance.user.username}. ' \
                  f'Появилась новый пост'
        message = f'Здравствуйте, {instance.user.username}. ' \
                  f'Появилась новый пост'
        send_mail(
            subject=subject,
            message=message,
            from_email='sev7engallon@yandex.ru',
            recipient_list=[user.email]
        )


class PostView(ListView):
    model = Post
    template_name = 'postlist.html'
    context_object_name = 'postlist'
    ordering = ['-time_emerged']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authed'] = self.request.user.is_authenticated
        context['profile'] = self.request.user
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        post_id = Post.objects.get(id=id)
        context['author'] = post_id.author.user.id
        context['curr_user'] = self.request.user.id


class PostSearch(ListView):
    model = Post
    template_name = 'postsearch.html'
    context_object_name = 'postsearch'
    ordering = ['-time_emerged']
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['is_authed'] = self.request.user.is_authenticated
        return context


class AuthorDetail(DetailView,):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authed'] = self.request.user.is_authenticated
        context['curr_user'] = self.request.user.id
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'account/profile_update.html'
    form_class = ProfileForm
    success_url = '/'
    # id = Author
    # success_url = reverse_lazy('author_detail', args=[User.objects.get(username =id).id])

    def get_object(self, **kwargs):
        cur_user = self.request.user
        # if self.request.user.is_authenticated:
        id = self.kwargs.get('pk')
        return User.objects.get(pk=id)
        # else:
        #     return redirect('/accounts/login/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context


class PostAddView(CreateView, LoginRequiredMixin):
    template_name = 'post_add.html'
    form_class = PostForm

    # def form_valid(self, form):
    #     category_id = self.request.POST.get('category')
    #     post_text = self.request.POST.get('text')
    #     post_name = self.request.POST.get('name')
    #     post_image = self.request.POST.get('image')
    #     text_content = f' | {post_name} | \n{post_text[:50]}...'
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authed'] = self.request.user.is_authenticated
        return context


class PostUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'post_add.html'
    form_class = PostForm
    success_url = '/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления
class PostDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/'


class MessageView(CreateView, LoginRequiredMixin):
    template_name = 'msg_add.html'
    form_class = MessageForm
    success_url = '/'

    def form_valid(self, form):
        new_msg = form.save(commit=False)
        new_msg.post = self.post
        new_msg.user = self.request.user
        new_msg.save()
        return super().form_valid(form)


class MsgView(ListView, LoginRequiredMixin):
    model = Message
    template_name = 'msglist.html'
    context_object_name = 'msglist'
    ordering = ['-time_emerged']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authed'] = self.request.user.is_authenticated
        context['profile'] = self.request.user
        return context


@login_required
def msg_submit(request, pk):
    msg = Message.objects.get(id=pk)
    if not msg.submitted:
        msg.submitted = True





@login_required
def make_author(request):
    user = request.user
    # authors_group = Author.objects.get(name='authors')
    if not Author.objects.filter(user_id=user.id).exists():
        Author.user_set.add(user)
    return redirect('/')
