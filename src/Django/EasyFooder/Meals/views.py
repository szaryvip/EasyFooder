from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader_tags
from django.template import loader
from django.shortcuts import  render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import OrderForm

from .models import Order
from Meals.models import Meal


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
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                meal_id = form.cleaned_data["meal_id"]
                meal = Meal.objects.get(meal_id=meal_id)
                user = User.objects.get(id=1)
                order = Order(
                    user_id=user, order_id=9001, date="2077-09-09 12:00",
                    status="leci se", meal_id=meal
                )
                order.save()
                return HttpResponseRedirect('orders')
        elif request.method == 'GET':
            form = OrderForm()

        suggestions = Meal.objects.all().values()
        return render(
            request, 'make_order.html', {
                'form': form, 'suggestions': suggestions
            }
        )
    else:
        return redirect('login')
