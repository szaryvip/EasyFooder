from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import OrderForm
from Users.recommendation import recommend

from datetime import datetime, timezone, timedelta
from .models import Order
from Meals.models import Meal


def meals(request):
    if request.user.is_authenticated:
        meals = Meal.objects.all().values()
        template = loader.get_template('meals.html')
        context = {
            'meals': meals
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/users/login')


def orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user_id=request.user)
        for order in orders:
            if order.date < datetime.now().replace(tzinfo=timezone.utc) -\
               timedelta(minutes=15):
                order.status = "W drodze"
                order.save()
            if order.date < datetime.now().replace(tzinfo=timezone.utc) -\
               timedelta(minutes=40):
                order.status = "Dostarczono"
                order.save()

        template = loader.get_template('orders.html')
        context = {
            'orders': orders
        }

        return HttpResponse(template.render(context, request))
    else:
        return redirect('/users/login')


def make_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                meal = form.cleaned_data["meal"]
                user = request.user
                order = Order(
                    user_id=user,
                    date=datetime.now().replace(
                        tzinfo=timezone.utc
                    ),
                    status="Zamówiono", meal_id=meal
                )
                order.save()
                return redirect('orders')
        elif request.method == 'GET':
            form = OrderForm()

        suggestions = recommend(request.user, User.objects.all())
        return render(
            request, 'make_order.html', {
                'form': form, 'suggestions': suggestions
            }
        )
    else:
        return redirect('/users/login')
