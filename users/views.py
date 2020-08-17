from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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
        # save values from the form
        # get the check marked boxes
        # put all info in a list
        # Profile.set_profile method
        p_form = ProfileUpdateForm(request.POST)
        if p_form.is_valid():
            user_profile = p_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('preferences')
    p_form = ProfileUpdateForm()
    context = {
        'p_form': p_form
    }
    return render(request, 'users/preferences.html', context)