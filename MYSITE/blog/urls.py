from django.urls import path

from . import views

urlpatterns = [
    path(
        '', 
        views.blog_list, 
        name='blog_list'
    ),
    path(
        'blog/category/<slug:slug>/', 
        views.blog_list, 
        name='blog_list_by_category'
    ),
    
    
    # post manage
    path(
        'blog/create-post/', 
        views.blog_create, 
        name='blog_create'
    ),
    path(
        'blog/edit-post/<int:post_id>/', 
        views.blog_edit, 
        name='blog_edit'
    ),
    
    # reply
    path(
        'blog/post/reply-create/<int:post_id>/', 
        views.reply_create, 
        name='reply_create'
    ),
    path(
        'blog/post/reply-list/', 
        views.reply_list, 
        name='reply_list'
    ),
    path(
        'blog/post/reply-list/<int:post_id>/', 
        views.reply_list, 
        name='reply_list_filter'
    ),
    path(
        'blog/post/reply-delete/<int:reply_id>/', 
        views.reply_delete, 
        name='reply_delete'
    ),
    path(
        'blog/post/reply_confirm/<int:reply_id>/', 
        views.reply_confirm, 
        name='reply_confirm'
    ),
]