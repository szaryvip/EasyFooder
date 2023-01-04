from django import forms
from Meals.models import Meal


class OrderForm(forms.Form):
    meals = Meal.objects.all().values()
    meals = [(meal['meal_id'], meal['name']) for meal in meals]
    meal_id = forms.ChoiceField(choices=meals)
