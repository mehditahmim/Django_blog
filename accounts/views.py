from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            if user:
                return HttpResponseRedirect(reverse('landing:index'))

        else:
            return render(request, 'accounts/signup.html', {'form': form})

    else:
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})


"""def home(request):
    return render(request, 'index.html')
"""


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse('landing:index'))
        else:
            return render(request, 'accounts/login.html', {'form': form, 'error_message': "The username or password is wrong!"}, )
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
