from django.http import HttpResponse
from django.template import loader
from .models import Order
from Meals.models import Meal
from Users.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import OrderForm


def orders(request):
    orders = Order.objects.all().values()
    meals = Meal.objects.all().values()

    template = loader.get_template('orders.html')
    context = {
        'orders': orders,
        'meals': meals
    }

    return HttpResponse(template.render(context, request))


def make_order(request):
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
            user = User.objects.get(user_id=1)
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
