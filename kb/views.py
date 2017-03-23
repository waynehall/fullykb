from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from userDir.models import Profile
# Create your views here.

@login_required
def index(request):
    all_profiles = User.objects.all().select_related('profile')
    context = {
        'all_profiles': all_profiles
    }
    return render(request, 'kb/content.html', context)