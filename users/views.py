from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from self import self

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. Log In')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)


@login_required()
def preferences(request):
    if request.method == 'POST':
        print(request.POST)
        Profile.set_profile(self, ['test'])
        # save values from the form
        # get the check marked boxes
        # put all info in a list
        # Profile.set_profile method
    p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'p_form': p_form
    }
    return render(request, 'users/preferences.html', context)