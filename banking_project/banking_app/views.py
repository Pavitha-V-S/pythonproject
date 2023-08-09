from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .django import UserProfileForm
from .models import UserProfile


def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('user_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    selected_materials = user_profile.materials_provided.split(', ') if user_profile.materials_provided else []

    return render(request, 'userprofile.html', {
        'user': user,
        'user_profile': user_profile,
        'selected_materials': selected_materials,
    })
