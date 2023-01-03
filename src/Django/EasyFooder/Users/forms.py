from django import forms


class OrderForm(forms.Form):
    meal_id = forms.IntegerField(label='meal_id')
