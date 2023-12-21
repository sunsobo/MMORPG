from django.conf import settings
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives


from .models import Profile


# BEGIN email confirm send
def email_confirm_send(request, user_id, token_generator):
    
    new_user = User.objects.get(id=user_id)
    
    domain = 'www.' + settings.SITE_URL
    
    subject = 'Подтверждение адреса электронной почты {}'.format(domain)
    from_email = settings.EMAIL_HOST_USER
    to = str(new_user.email)
    text_content = 'Подтверждение адреса электронной почты на {}'.format(domain)

    t1 = '<p>Вы получили это письмо, потому что вы (или кто-то другой) запросили '
    t2 = 'подтверждение электронной почты учётной записи на сайте {}</p>'.format(domain)
    t3 = 'Чтобы подтвердить свой Email, перейдите по ссылке <a href="https://{}/accounts/email-confirm/'.format(domain)
    t4 =  str(token_generator) + '/' + str(new_user.id) + '/">{}/accounts/email-confirm/'.format(domain) + str(token_generator) + '/' + str(new_user.id) + '/</a>'
    t5 = '<p>Спасибо, что используете наш сайт!</p> <p>Команда сайта {}</p>'.format(domain)
    html_content = str(t1 + t2 + t3 + t4 + t5)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
# END email confirm send




# BEGIN email_send
def email_send(subject, to, text_content, html_content):
    domain = 'www.' + settings.SITE_URL
    from_email = settings.EMAIL_HOST_USER
    
    if type(to) is str:
        to = [to]
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
# END email_send