from django.conf import settings

from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponseRedirect


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# from django.http import JsonResponse

from django.urls import reverse
from django.utils import timezone
from datetime import timedelta


from django.contrib.auth.models import User

# PAGINATOR
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# SEARCH
from django.db.models import Q


from .models import Profile
from .forms import LoginForm, SignUpForm
from .forms import ProfileForm, MassEmailForm


from .decorators import login_redirect


import uuid
from django.utils.crypto import get_random_string

# from urllib.parse import unquote


from .checks import email_confirm_send
from .checks import email_send

# BEGIN user_signup
@login_redirect
def user_signup(request):
    title = 'Регистрация'
    if request.method == 'POST':
        form = SignUpForm(
            request.POST
        )
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()

            chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
            token_generator = get_random_string(23, chars)
    
            new_user.profile.email_token = token_generator
            new_user.profile.email_token_date = timezone.now()
            new_user.profile.save()
            email_confirm_send(request, new_user.id, token_generator)
            
            messages.success(request, 'На ваш Email отправлено письмо для подтверждения почты.')
            return HttpResponseRedirect(
                            reverse('user_login', args=[])
                        )
    else:
        form = SignUpForm()

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
# END user_signup



# BEGIN user_login
@login_redirect
def user_login(request):
    title = 'Вход в систему'
    
    user_auth = None
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_auth = authenticate(
                username=cd['username'],
                password=cd['password']
            )
            if user_auth is None:
                messages.error(request, 'Неправильный логин или пароль.')
            else:
                if user_auth.profile.email_confirm == False:
                    messages.warning(request, 'Для входа подтвердите эл. почту!')
                else:
                    login(request, user_auth)
                    
                    next = request.GET.get('next')
                    if next:
                        return redirect(next)
                    else:
                        return HttpResponseRedirect(
                            reverse('blog_list', args=[])
                        )
    else:
        form = LoginForm()

    context = {
        'title': title,
        'form': form,
        'user_auth': user_auth,
    }
    return render(request, 'accounts/login.html', context)
# END user_login




# BEGIN user_logout
@login_required
def user_logout(request):
    logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    else:
        return redirect('/')
# END user_logout





# BEGIN email_confirm
def email_confirm(request, token, user_id):
    
    title = 'Подтверждение почты'
    
    user_an = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user_an)
    
    date = timezone.now() - timedelta(days=14)
    
    if profile.email_token == token and profile.email_token_date > date:
        profile.email_confirm = True
        profile.save()
        
        context = {
            'title': title,
        }
        
        return render(request, 'accounts/email_confirm.html', context)
    else:
        return redirect('/')
# END email_confirm




# BEGIN email_send_again
def email_send_again(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if user.email:
        if user.profile.email_confirm == True:
            messages.success(request, 'Эл. почта уже подтверждена!')
        else:
            chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
            token_generator = get_random_string(23, chars)
    
            user.profile.email_token = token_generator
            user.profile.email_token_date = timezone.now()
            user.profile.save()
            email_confirm_send(request, user.id, token_generator)
    
            messages.success(request, 'На ваш Email отправлено письмо для подтверждения почты.')
    else:
        messages.error(request, 'Отсутствует эл. почта!')
    return HttpResponseRedirect(
                                    reverse(
                                        'user_login',
                                        args=[]
                                    )
                                )
# END email_send_again




# BEGIN user_edit
@login_required
def user_edit(request):
    title = 'Редактировать профиль'
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            
            messages.success(request, 'Данные успешно сохранены.')
            return HttpResponseRedirect(
                            reverse('user_edit', args=[])
                        )
    else:
        form = ProfileForm(
            instance=profile,
        )

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'accounts/form.html', context)
# END user_edit




# BEGIN mass_mail
@staff_member_required
def mass_mail(request):
    title = 'Новостная рассылка'
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        form = MassEmailForm(
            request.POST,
        )
        if form.is_valid():
            cd = form.cleaned_data
            
            title = cd['title']
            text = cd['text']
            
            user_list = User.objects.all()
            email_list = []
            for u in user_list:
                email_list.append(u.email)
                
            domain = 'www.' + settings.SITE_URL
            subject = title
            to = email_list
            text_content = subject
            html_content = text
            
            email_send(subject, to, text_content, html_content)
            
            messages.success(request, 'Письма успешно отправлены.')
            return HttpResponseRedirect(
                            reverse('mass_mail', args=[])
                        )
    else:
        form = MassEmailForm()

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'accounts/form.html', context)
# END mass_mail






