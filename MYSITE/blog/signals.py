from django.conf import settings

from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import PostReply

from accounts.checks import email_send
# def email_send(request, subject, to, text_content, html_content):

# when PostReply create
@receiver(post_save, sender=PostReply)
def create_reply(sender, instance, created, **kwargs):
    if created:
        domain = 'www.' + settings.SITE_URL
        
        subject = 'Новый отклик на ваше объявление'
        to = instance.post.user.email
        text_content = subject
        
        t1 = '<p>Пользователь {} отправил новый отклик на ваше объявление '.format(instance.user.username)
        t2 = ''
        t3 = ''
        t4 = ''
        t5 = '<p>Спасибо, что используете наш сайт!</p> <p>Команда сайта {}</p>'.format(domain)
        html_content = str(t1 + t2 + t3 + t4 + t5)
        
        email_send(subject, to, text_content, html_content)



# when PostReply save
@receiver(post_save, sender=PostReply)
def save_reply(sender, instance, **kwargs):
    if instance.confirm_mark == True:
    	domain = 'www.' + settings.SITE_URL
    	subject = 'Ваш отклик принят'
    	to = instance.user.email
    	text_content = subject
    
    	t1 = '<p>Пользователь {} принял ваш отклик. '.format(instance.post.user.username)
    	t2 = 'Объявление: {}'.format(instance.post.title)
    	t3 = ''
    	t4 = ''
    	t5 = '<p>Спасибо, что используете наш сайт!</p> <p>Команда сайта {}</p>'.format(domain)
    	html_content = str(t1 + t2 + t3 + t4 + t5)
    
    	email_send(subject, to, text_content, html_content)