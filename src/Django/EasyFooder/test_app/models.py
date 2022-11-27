from django.db import models


class Tag(models.Model):
    tag_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Meal(models.Model):
    meal_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70)

    tags = models.ManyToManyField(Tag, through='Meal_Tag')

# Association
class Meal_Tag(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    orders = models.ManyToManyField(Meal, through='Order')

# Association
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    date = models.DateField()

# Legacy class:
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

# Lengths:
# 0123456789 - 10
# 01234567890123456789 - 20
# 012345678901234567890123456789 - 30
# 01234567890123456789012345678901234567890123456789 - 50
