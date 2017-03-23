from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from kb.views import index
from django.template import RequestContext
from .forms import ProfileForm
from django.db import transaction
from .models import Profile
from django.contrib import messages

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse('/kb')
            else: 
                return HttpResponse("You don't have an account.")
        else:
            print("invalid login")
            return HttpResponse("Invalid person")
    else:
        return render(request, 'userDir/login.html')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method =='POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else: messages.error(request, _('please correct the error'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })