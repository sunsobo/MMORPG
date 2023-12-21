from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import PostCategory, Post, PostReply

from .forms import PostForm, PostReplyForm

# BEGIN blog_list
@login_required
def blog_list(request, slug=None):
    title = 'Доска объявлений'
    
    # category check
    if slug:
        category = get_object_or_404(PostCategory, slug=slug)
        post_list = Post.objects.filter(
            category__slug=slug)
    else:
        category = None
        post_list = Post.objects.all()
        
    category_list = PostCategory.objects.all()
    
    # search
    query = request.GET.get("q")
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
        ).distinct()
    
    # paginator
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page', 1)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    
    context = {
        'title': title,
        'category': category,
        'category_list': category_list,
        'post_list': post_list,
        'query': query,
    }
    return render(request, 'blog/list.html', context)
# END blog_list



# BEGIN blog_create
@login_required
def blog_create(request):
    title = 'Создать объявление'
    
    if request.method == 'POST':
        form = PostForm(
            request.POST
        )
        if form.is_valid():
            cd = form.save(commit=False)
            cd.user = request.user
            cd.save()
            
            messages.success(request, 'Объявление успешно создано.')
            return HttpResponseRedirect(
                            reverse('blog_list', args=[])
                        )
    else:
        form = PostForm()
    
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'blog/form.html', context)
# END blog_create



# BEGIN blog_edit
@login_required
def blog_edit(request, post_id):
    title = 'Редактировать объявление'
    
    post = get_object_or_404(Post, id=post_id)
    
    if request.user != post.user:
        messages.error(request, 'Ошибка! Нельзя редактировать чужой пост.')
        return HttpResponseRedirect(
                        reverse('blog_list', args=[])
                    )
    
    if request.method == 'POST':
        form = PostForm(
            request.POST,
            instance=post,
        )
        if form.is_valid():
            cd = form.save(commit=False)
            cd.save()
            
            messages.success(request, 'Объявление успешно отредактировано.')
            return HttpResponseRedirect(
                            reverse('blog_list', args=[])
                        )
    else:
        form = PostForm(
            instance=post,
        )
    
    context = {
        'title': title,
        'form': form,
        'post': post,
    }
    return render(request, 'blog/form.html', context)
# END blog_edit




# BEGIN reply_create
@login_required
def reply_create(request, post_id):
    title = 'Отправить отклик'
    
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = PostReplyForm(
            request.POST
        )
        if form.is_valid():
            cd = form.save(commit=False)
            cd.user = request.user
            cd.post = post
            cd.save()
            
            messages.success(request, 'Отклик успешно отправлен.')
            return HttpResponseRedirect(
                            reverse('blog_list', args=[])
                        )
    else:
        form = PostReplyForm()
    
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'blog/form.html', context)
# END reply_create



# BEGIN reply_list
@login_required
def reply_list(request, post_id=None):
    title = 'Отклики на объявления'
    user = request.user
    
    reply_list = PostReply.objects.filter(post__user=user)
    
    post_list = Post.objects.filter(user=user)
    if post_id:
        reply_list = PostReply.objects.filter(
            post__user=user, 
            post__id=post_id,
        )
    
    # search
    query = request.GET.get("q")
    if query:
        reply_list = reply_list.filter(
            Q(post__title__icontains=query) |
            Q(post__text__icontains=query)
        ).distinct()
    
    context = {
        'title': title,
        'reply_list': reply_list,
        'post_list': post_list,
        'query': query,
    }
    return render(request, 'blog/reply_list.html', context)
# END reply_list



# BEGIN reply_delete
@login_required
def reply_delete(request, reply_id):
    title = 'Удалить отклик'
    user = request.user
    
    reply = get_object_or_404(PostReply, id=reply_id)
    
    if user != reply.post.user:
        return HttpResponseRedirect(
                    reverse('blog_list', args=[])
                )
                
    reply.delete()
    
    context = {
        'title': title,
    }
    messages.success(request, 'Отклик успешно удален.')
    return HttpResponseRedirect(
                    reverse('reply_list', args=[])
                )
# END reply_delete



# BEGIN reply_confirm
@login_required
def reply_confirm(request, reply_id):
    title = 'Принять отклик'
    user = request.user
    
    reply = get_object_or_404(PostReply, id=reply_id)
    
    
    if user != reply.post.user:
        return HttpResponseRedirect(
                    reverse('blog_list', args=[])
                )
                
    reply.confirm_mark = True
    reply.save()
    
    context = {
        'title': title,
    }
    messages.success(request, 'Отклик успешно принят.')
    return HttpResponseRedirect(
                    reverse('reply_list', args=[])
                )
# END reply_confirm