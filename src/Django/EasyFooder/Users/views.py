from django.http import HttpResponse
from django.template import loader
from .models import Order
from Meals.models import Meal

def members(request):
  orders = Order.objects.all().values()
  meals = Meal.objects.all().values()

  template = loader.get_template('orders.html')
  context = {
    'orders': orders,
    'meals': meals
  }

  return HttpResponse(template.render(context, request))