from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Message, User, Post


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

