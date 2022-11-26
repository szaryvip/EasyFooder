from django.db import models

# Sztuczna klasa:
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

# Prawdziwe klasy:
class User(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

class Order(models.Model):
    date = models.DateField()

class Tag(models.Model):
    id_tag = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Meal(models.Model):
    id_meal = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)

    tags = models.ManyToManyField(
        Tag,
        through='Meal_Tag',
        through_fields=('id_meal', 'id_tag')
    )

class Meal_Tag(models.Model):
    id_meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    id_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
