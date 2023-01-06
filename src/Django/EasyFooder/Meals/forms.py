from django import forms
from Meals.models import Meal


class OrderForm(forms.Form):
    meal = forms.ModelChoiceField(queryset=Meal.objects.all(), initial=0)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['meal'].label_from_instance = lambda instance: instance.name
        self.fields['meal'].label = ""