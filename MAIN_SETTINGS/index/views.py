from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# BEGIN index
@login_required
def index(request):
    title = 'Главная'
    
    context = {
        'title': title,
    }
    return render(request, 'index/index.html', context)
# END index