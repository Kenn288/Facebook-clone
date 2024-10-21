from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserRegisterForm, UserLoginForm, UserProfileEditForm, UserPasswordChangeForm
from .models import UserProfile

# User Registration View

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created and you are now logged in.")
            return redirect('profile', username=user.username)
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

# User Login View
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('profile', username=user.username)
        messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})

# User Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')

# User Profile View
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.post_set.all()  # Assuming you have a Post model related to the User
    return render(request, 'core/profile.html', {'user': user, 'posts': posts})

# Edit Profile View
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('profile', username=request.user.username)
    else:
        form = UserProfileEditForm(instance=request.user.userprofile)
    return render(request, 'core/edit_profile.html', {'form': form})

# Password Change View
@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed.")
            return redirect('profile', username=request.user.username)
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'core/change_password.html', {'form': form})
