from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import OrderForm
from Users.recommendation import recommend
from django.db.models import Max

from datetime import datetime
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
        orders = Order.objects.all().values()
        meals = Meal.objects.all().values()

        template = loader.get_template('orders.html')
        context = {
            'orders': orders,
            'meals': meals
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
                orders = Order.objects.all()
                order_id = orders.aggregate(Max('order_id'))['order_id__max'] + 1 if orders else 1
                order = Order(
                    user_id=user, order_id=order_id,
                    date=datetime.now().strftime("%Y-%m-%d %H:%M"),
                    status="Zamówiono", meal_id=meal
                )
                order.save()
                return HttpResponseRedirect('orders')
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
