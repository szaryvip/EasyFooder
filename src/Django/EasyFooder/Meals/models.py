from django.db import models
from django.contrib.auth.models import User


class Meal(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(decimal_places=2, max_digits=6)


class Tag(models.Model):
    name = models.CharField(max_length=15)


class Meal_tag(models.Model):
    tag = models.ForeignKey('Meals.Tag', on_delete=models.CASCADE)
    meal = models.ForeignKey('Meals.Meal', on_delete=models.CASCADE)


class Order(models.Model):
    date = models.DateTimeField()
    status = models.CharField(max_length=15)
    meal_id = models.ForeignKey('Meals.Meal', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
