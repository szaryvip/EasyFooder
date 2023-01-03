from django.db import models
from Meals.models import Meal

class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    
    
class Order(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField()
    status = models.CharField(max_length=15)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
