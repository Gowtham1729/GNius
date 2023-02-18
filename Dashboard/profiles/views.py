from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm, UserProfileForm


def register(request):
    form = UserForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None)
    if form.is_valid() and profile_form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        profile = profile_form.save(commit=False)
        user.save()
        profile.user = user
        profile.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('terashare:home')
    context = {
        "form": form,
        "profile_form": profile_form
    }
    return render(request, 'profiles/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home:home')
            else:
                return render(request, 'profiles/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'profiles/login.html', {'error_message': 'Invalid login'})
    return render(request, 'profiles/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None)
    context = {
        "form": form,
        "profile_form": profile_form
    }
    return render(request, 'profiles/login.html', context)

def home(request):
    return render(request, 'profiles/home.html')
