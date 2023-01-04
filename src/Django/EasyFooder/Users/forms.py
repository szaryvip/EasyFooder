from django import forms
from Meals.models import Meal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(forms.Form):
    meals = Meal.objects.all().values()
    meals = [(meal['meal_id'], meal['name']) for meal in meals]
    meal_id = forms.ChoiceField(choices=meals)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user
