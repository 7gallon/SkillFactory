from django.contrib.auth.models import User
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from datetime import datetime
from .models import CategoryUser, Category, Post
from django.core.mail import send_mail


@shared_task
def new_post_email(text_content, suber_id):
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


@shared_task
def weekly_post_email():
    # this_week_category_articles
    prev_week = datetime.datetime.now() - datetime.timedelta(days=7)
    cats = Category.objects.all()
    for cat in cats:
        subscribers = CategoryUser.objects.filter(category=cat)
        posts = Post.objects.filter(category=cat, time_emerged__gte=prev_week)
        msg_posts = ''
        if len(posts) != 0:
            for post in posts:
                msg_posts += f'{post.name} {post.time_emerged} {post.preview()} \n'
            # if cat.subscribers != 'auth.User.None':
            for sub in subscribers:
                print('sending...')
                print(sub.user.email)

                send_mail(
                    subject=f'Weekly News Update for you, {sub}',
                    message=f'Here are the last week news on your favourite categories: \n' + msg_posts,
                    from_email='sev7engallon@yandex.ru',
                    recipient_list=[sub.user.email],
                )
                print('*******************************************************************************************')
    print('Done sending emails')
