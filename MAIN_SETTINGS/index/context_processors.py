from django.core.exceptions import PermissionDenied

def index(request):
    user = request.user
    
    SITE_NAME = 'MMORPG - Доска объявлений'

    context = {
        'user': user,
        'SITE_NAME': SITE_NAME,
    }
    return (context)