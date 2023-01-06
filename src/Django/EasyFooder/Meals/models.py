from django.db import models
from django.contrib.auth.models import User


class Meal(models.Model):
    meal_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __repr__(self):
        return f"Meal: {self.name}"


class Tag(models.Model):
    tag_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=15)

    def __repr__(self):
        return f"TEST: {self.name}"


class Meal_tag(models.Model):
    tag = models.ForeignKey('Meals.Tag', on_delete=models.CASCADE)
    meal = models.ForeignKey('Meals.Meal', on_delete=models.CASCADE)


class Order(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField()
    status = models.CharField(max_length=15)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
