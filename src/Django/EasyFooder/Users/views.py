from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm


def index(request):
    if request.user.is_authenticated:
        template = loader.get_template('index.html')
        context = {
            'login': request.user.username
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration succesfull")
            return redirect('login')
        messages.error(request,
                       "Unsuccessful registration. Invalid information.")
    else:
        form = RegisterForm()

    return render(
        request, 'register.html', {'form': form}
    )


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(
        request, 'login.html', {'form': form}
    )


def logout(request):
    django_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")
