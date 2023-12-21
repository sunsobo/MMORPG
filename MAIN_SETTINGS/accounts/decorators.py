from django.shortcuts import redirect




# BEGIN login redirect
def login_redirect(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if user.is_authenticated:
            return redirect('/')
        else:
            return function(request, *args, **kw)
    return wrapper
# END login redirect