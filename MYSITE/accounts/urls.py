from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path(
        'accounts/login/', 
        views.user_login, 
        name='user_login'
    ),
    path(
        'accounts/logout/', 
        views.user_logout, 
        name='user_logout'
    ),
    
    path(
        'accounts/signup/', 
        views.user_signup, 
        name='user_signup'
    ),
    
    
    # email confirm
    path(
        'accounts/email-send-again/<int:user_id>/',
        views.email_send_again,
        name='email_send_again',
    ),
    
    
    # user_edit / profile_edit
    
    path(
        'accounts/user-email-confirm/', 
        views.user_email_confirm, 
        name='user_email_confirm'
    ),
    path(
        'accounts/user-edit/', 
        views.user_edit, 
        name='user_edit'
    ),
    
    
    # email mass send
    path(
        'accounts/email-mass-send/', 
        views.mass_mail,
        name='mass_mail'
    ),
]