from django.http import HttpResponse
from django.template import loader
from django.shortcuts import  render, redirect
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages
from .models import Order
from Meals.models import Meal

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import OrderForm, RegisterForm

def index(request):
    if request.user.is_authenticated:
        template = loader.get_template('index.html')
        context = {
            'login': request.user.username
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('login')
        

def orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.all().values()
        meals = Meal.objects.all().values()

        template = loader.get_template('orders.html')
        context = {
            'orders': orders,
            'meals': meals
        }

        return HttpResponse(template.render(context, request))
    else:
        return redirect('login')


def make_order(request):
    if request.user.is_authenticated:
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = OrderForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                meal_id = form.cleaned_data["meal_id"]
                meal = Meal.objects.get(meal_id=meal_id)
                user = User.objects.get(id=1)
                order = Order(
                    user_id=user, order_id=9001, date="2077-09-09 12:00",
                    status="leci se", meal_id=meal
                )
                order.save()
                return HttpResponseRedirect('orders')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = OrderForm()

        # TODO: use actual suggestions
        suggestions = Meal.objects.all().values()
        return render(
            request, 'make_order.html', {'form': form, 'suggestions': suggestions}
        )
    else:
        return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration succesfull")
            return redirect('login')
        messages.error(request, "Unsuccessful registration. Invalid information.")
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
                return redirect('/users')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(
        request, 'login.html', {'form': form}
    )


def logout(request):
    django_logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")
