
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import PostCategory, Category, User


@receiver(post_save, sender=PostCategory)
def notify_category_subscribers(sender, instance, created, **kwargs):

    for suber in Category.subscribers.all():
        subject = f'Здравствуйте, {instance.suber.username}. ' \
                  f'Появилась новая статья в категории {instance.category.name}'
        send_mail(
            subject=subject,
            from_email='sev7engallon@yandex.ru',
            recipient_list=[suber.email]
        )

        return print(f'{suber.email} {instance.suber.username} {instance.category.name}')


@receiver(post_save, sender=User)
def registration_greeting(sender, instance, created, **kwargs):

    subject = f'NewsPortal приведствует {instance.username}. '
    message = f'Благодарим Вас за регистрацию на нашем портале!'
    send_mail(
        subject=subject,
        message=message,
        from_email='sev7engallon@yandex.ru',
        recipient_list=[instance.email]
    )

    return print(f'{instance.email} {instance.username}')
