from django.shortcuts import render
from medals.models import FullyUser
# Create your views here.

def index(request):
    all_users = FullyUser.objects.all()
    context = {
        'all_users': all_users,
    }
    return render(request, 'kb/content.html', context)