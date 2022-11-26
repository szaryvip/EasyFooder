from django.db import models

# Create your models here.


# Sztuczna klasa:
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

# Prawdziwe klasy:
class Tag(models.Model):
    tag_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Meal(models.Model):
    meal_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)

    tags = models.ManyToManyField(
        Tag,
        through='Meal_Tag'
    )

class Meal_Tag(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

    orders = models.ManyToManyField(
        Meal,
        through='Order'
    )

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    date = models.DateField()
